def pre_condition():
    converted_firm = input("Are there Converted Firms ? ")
    foreign_partners = input("Are there foreign partners ? ")
    gulf_partners = input("Are there gulf partners ? ")
    saudi_minor_partners = input("Are there saudi minor partners ? ")
    saudi_disable_partners = input("Are there saudi disable partners ? ")
    gulf_manager_companies_partner = input("Are there gulf manager companies partner ? ")
    foreign_gulf_manager_companies_partner = input("Are there foreign or/and Gulf managers companies partner ? ")

    if ((converted_firm == 1) | (foreign_partners == 1) | (gulf_partners == 1) | (saudi_minor_partners == 1) |
        (saudi_disable_partners == 1) | (gulf_manager_companies_partner == 1) |
            (foreign_gulf_manager_companies_partner == 1)):
        return 0
    else:
        return 1


def validate_after_auto_approval():
    validate_after_auto_approval.partners_cmp_saudi_more_than_one = input("Are there partners of type Saudi "
                                                                          "Companies have more than one partner ? ")
    validate_after_auto_approval.partners_gov_ecr_saudi = input("Are there partners of type gov ecr saudi  ? ")
    validate_after_auto_approval.contract_extra_item = input("Are there contract added extra item(s) ? ")
    validate_after_auto_approval.contract_edit_item_text = input("Are there edit in item(s) text ? ")

    if ((validate_after_auto_approval.partners_cmp_saudi_more_than_one == 1) |
            (validate_after_auto_approval.partners_gov_ecr_saudi == 1)
            | (validate_after_auto_approval.contract_extra_item == 1) |
            (validate_after_auto_approval.contract_edit_item_text == 1)):
        return 0
    else:
        return 1


def auto_approval_form():
    # all_partners_individuals = input("Are all partners are individuals ? ")
    #
    # if all_partners_individuals == 1:
    #     print('No Attachment Needed; Send OTP to Individual Partners')
    # else:

        if validate_after_auto_approval.partners_cmp_saudi_more_than_one == 0:

            print(' No Attachments Needed, Send Request to Contract Reviewer')

        else:
            print('Go to Validate Managers of Company has more than one Partners')
            cmp_more_than_one_cmp_has_saudi_manager_has_privileges = input("Are one of partners is cmp partners "
                                                                           "with more than one partner "
                                                                           "and has saudi manager has privileges ? ")

            cmp_more_than_one_cmp_has_resident_manager_has_privileges = input("Are one of partners is cmp partners "
                                                                              "with more than one partner and"
                                                                              "has resident manager has privileges ?")

            if ((validate_after_auto_approval.partners_cmp_saudi_more_than_one == 1) &
                ((cmp_more_than_one_cmp_has_saudi_manager_has_privileges == 0) &
                (cmp_more_than_one_cmp_has_resident_manager_has_privileges == 0))):

                print('Go to Validate Partners')
                validate_partners_partner_cmp()

            elif ((validate_after_auto_approval.partners_cmp_saudi_more_than_one == 1) &
                  ((cmp_more_than_one_cmp_has_saudi_manager_has_privileges == 1) |
                  (cmp_more_than_one_cmp_has_resident_manager_has_privileges == 1))):
                print('No documents Needed, Send Request to Contract Reviewer then OTP To Saudi or Resident')


def validate_partners_partner_cmp():
    # cmp_partner_partner_type_is_ecr_or_s_individual_or_one_cmp = input("Are one of partners is cmp partners with "
    #                                                                    "more than one partner "
    #                                                                    "and partner type is ecr "
    #                                                                    "or Individuals or One Saudi Company? ")

    # cmp_partner_partner_type_is_saudi_individuals = input("Are one of partners is cmp partners "
    #                                                       "with more than one partner "
    #                                                       "and partner type is Saudi Individual ?  ")
    #
    # cmp_partner_partner_type_is_one_saudi_cmp = input("Are one of partners is cmp partners "
    #                                                   "with more than one partner "
    #                                                   "and partner type is One Partner Saudi Company ?   ")

    cmp_partner_partner_type_has_different_type = input("Are one of partners is cmp partners "
                                                        "with more than one partner "
                                                        "and partner type Not Saudi, Nor ECR, One Saudi?")

    if cmp_partner_partner_type_has_different_type == 0:
        print('No documents Needed. Send Request to Contract Reviewer then '
              'Send OTP to ECR Owner, Saudi Individuals or One Company Partner Owner')

    else:
        print('Please Attach Approval Documents and Send the Request to Contract Reviewer ')


Need_Auto_Approval = pre_condition()

if Need_Auto_Approval == 1:
    print('Yes Need Auto Approval, Lets validate Validation Cases for Reviewing')

    Need_Reviewing = validate_after_auto_approval()

    if Need_Reviewing == 1:
        print('Directly to Auto Approval')
    else:
        print('Reviewing needed by Contract Reviewer then Auto Approval')
    auto_approval_form()

else:
    print('No Auto Approval Needed, Request will assigned to Contract Reviewer then to Moj User')



