import csv

from enum import Enum


    def persist_to_db(self, line, file_name, line_no):
        charge_ari = self.get_value(line, TCIField.CHARGE_ARI)
        if self._is_none_and_log(file_name, line_no, charge_ari, 'charge_ari'):
            return
        charge_id = request.dbsession.query(Charge.id).filter_by_aris([charge_ari],
                                                                      Charge).scalar()
        if charge_id is None:
            self.log.warning(
                "File name: {}, line No.: {}, charge_id is not found:{}".format(file_name, line_no,
                                                                                charge_ari))
            return

        user_ari = self.get_value(line, TCIField.USER_ARI)
        if self._is_none_and_log(file_name, line_no, user_ari, 'user_ari'):
            return
        user_id = request.dbsession.query(User.id).filter_by_aris([user_ari], User).scalar()
        if user_id is None:
            self.log.warning(
                "File name: {}, line No.: {}, user_id is not found:{}".format(file_name, line_no,
                                                                              user_ari))
            return

        contact_date_str = self.get_value(line, TCIField.CONTACT_DATE)  # parse it to date.
        contact_date = self.str_to_date(contact_date_str)
        if contact_date is None:
            self.log.warning(
                "File name: {}, line No.: {}, contact_date is not valid:{}".format(file_name,
                                                                                   line_no,
                                                                                   contact_date_str))
            return

        # get phone id, if fail, create an entry.
        phone_number_raw = self.get_value(line,
                                          TCIField.PHONE_NUMBER)  # normalize, create one if cannot query it
        try:
            phone_number_standard = AffirmPhone(phone_number_raw)  # normalized.
        except ValueError as err:  # phone format error
            self.log.warning(
                "File name: {}, line No.: {}, phone_number is not valid:{}".format(file_name,
                                                                                   line_no,
                                                                                   phone_number_raw))
            return

        phone_number_id = request.dbsession.query(PhoneNumber.id).filter_by(
            phone_number=phone_number_standard,
            user_id=user_id).scalar()
        ccr = None
        if phone_number_id is None:  # not found, create one
            phone_number = PhoneNumber(phone_number=phone_number_standard,
                                       data_source=DataSource.tci, user_id=user_id)
            request.dbsession.add(phone_number)
            request.dbsession.flush()
            phone_number_id = phone_number.id
        else:
            ccr = request.dbsession.query(CSRContactRecord).filter_by(user_id=user_id,
                                                                      charge_id=charge_id,
                                                                      contact_phone_number_id=phone_number_id,
                                                                      contact_date=contact_date).first()

        if not ccr:
            ccr = CSRContactRecord(charge_id=charge_id, user_id=user_id, contact_date=contact_date,
                                   contact_phone_number_id=phone_number_id)
            request.dbsession.add(ccr)

        updates = {}

        call_outcome = self.get_value(line, TCIField.CALL_OUTCOME)
        if call_outcome:
            updates = {'call_outcome': self.get_value(line, TCIField.CALL_OUTCOME),
                       'contact_type': self.get_value(line, TCIField.CONTACT_TYPE),
                       'call_reason': self.get_value(line, TCIField.CALL_REASON),
                       'work_note': self.get_value(line, TCIField.WORK_NOTE),
                       'promise_to_pay_date': self.str_to_date(
                           self.get_value(line, TCIField.PROMISE_TO_PAY_DATE))}

        [setattr(ccr, key, val) for key, val in updates.iteritems()]
        request.dbsession.flush()
        return ccr

    def get_value(self, line, enum_field):
        """
        return None or striped string value
        """
        value = line.get(enum_field.value, '')
        return (value.strip() or None) if value is not None else value

    def str_to_date(self, date_str):
        if date_str is None:
            return None
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            return None
        except Exception as err:
            self.log.exception("Error in parse date:%s, not valid:%s", date_str, err)
            return None

    def _is_none_and_log(self, file_name, line_no, value, show_name):
        if value is None:
            self.log.warning(
                "File name: {}, line No.: {}, {} is None".format(file_name, line_no, show_name))
            return True
        return False






    filename = '/Users/yanzhibai/data/AffirmCom_TCI_20160302_RESULTS.csv'
    with open(filename) as csv_in:
        reader = csv.reader(csv_in)
        try:
            header_fields = reader.next()
            header_num = len(header_fields)
            worknote_index = header_fields.index(TCIField.WORK_NOTE.value)
        except Exception:
            print 'header exception'
            return

    for line_no, line_list in enumerate(reader, 1):
        if len(line_list) < header_num:
            print 'warning'
            continue

        if len(line_list) > header_num:
            diff = len(line_list) - header_num
            line_list = line_list[:worknote_index] + \
                         [','.join(line_list[worknote_index:worknote_index + diff + 1])] + \
                          line_list[worknote_index + diff + 1:]

        line_dict = dict(zip(header_fields, line_list))
        record = persist_to_db(line_dict, filename, line_no)


    class TCIField(Enum):
        USER_ARI = 'UserAri'
        CHARGE_ARI = 'ChargeARI'
        CONTACT_DATE = 'current_date'
        PHONE_NUMBER = 'phone_number'
        CONTACT_NUMBER = 'ContactNumber'
        CALL_OUTCOME = 'CallOutcome'
        CONTACT_TYPE = 'ContactType'
        CALL_REASON = 'CallReason'
        WORK_NOTE = 'WorkNote'
        PROMISE_TO_PAY_DATE = 'PromiseToPayDate'





