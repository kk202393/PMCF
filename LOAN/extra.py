# New System Design

class KYCIDS(models.Model):
    Aadhaar = models.BigIntegerField(unique=True)
    VoterCard = models.CharField(unique=True, max_length=50)
    OtherKYCIdtype = models.CharField(null=True, max_length=50)
    OtherKYCId = models.CharField(null=True, max_length=50)
    loanId = models.BigIntegerField()
    customerId = models.BigIntegerField()
    Application_No = models.BigIntegerField()
    

class Customer_Details(models.Model):
    LoanId = models.ForeignKey(KYCIDS,null=False,unique=True,on_delete=models.CASCADE)
    Aadhaar = models.BigIntegerField(unique=True)
    Custimage = models.ImageField(upload_to="img",default=None)
    Member_Aadhar_Card_front = models.ImageField(upload_to="img",default=None)
    Member_Aadhar_Card_back = models.ImageField(upload_to="img",default=None)
    Member_Voter_Card_front = models.ImageField(upload_to="img",default=None)
    Member_Voter_Card_back = models.ImageField(upload_to="img",default=None)
    Member_Bank_Details = models.ImageField(upload_to="img",default=None)
    Member_Relationship_Proof = models.ImageField(upload_to="img",default=None)
    FirstName = models.CharField(max_length=100 , default=None)
    LastName = models.CharField(max_length=100 , default=None)
    Gender = models.CharField(max_length=100 , default=None)
    DateOfBirth = models.DateField()
    Age = models.IntegerField(default=None)
    MaritalStatus = models.CharField(max_length=100 , default=None)
    FSName = models.CharField(max_length=100 , default=None)
    FSType = models.CharField(max_length=100 , default=None)
    FSDateOfBirth = models.DateField()
    FSAdhaar = models.BigIntegerField(unique=True , default=None)
    MothersName = models.CharField(max_length=100 , default=None)
    Caste = models.CharField(max_length=100 , default=None)
    Religion = models.CharField(max_length=100 , default=None)
    Qualification = models.CharField(max_length=100 , default=None)
    Occupation = models.CharField(max_length=100 , default=None)
    PhoneNumber = models.BigIntegerField(default=None)
    AddressLine1 = models.CharField(max_length=100 , default=None)
    AddressLine2 = models.CharField(max_length=100 , default=None)
    AddressLine3 = models.CharField(max_length=100 , default=None)
    PreferredLanguage = models.CharField(max_length=100 , default=None)
    Pincode = models.PositiveIntegerField(default=None)
    Village = models.CharField(max_length=100 , default=None)
    State = models.CharField(max_length=100 , default=None, choices=STATE_CHOICES)
    District = models.CharField(max_length=100,default=None, choices=District_CHOICES)
    confirmAddressLine1 = models.CharField(max_length=100  , default=None)
    confirmAddressLine2 = models.CharField(max_length=100 , default=None)
    confirmAddressLine3 = models.CharField(max_length=100 , default=None)
    confirmPincode = models.IntegerField(default=None)
    confirmVillage = models.CharField(max_length=100 , default=None)
    confirmState = models.CharField(max_length=100, choices=STATE_CHOICES , default=None)
    confirmDistrict = models.CharField(
        max_length=100, choices=District_CHOICES , default=None
    )
    Doc1image = models.ImageField(upload_to="img", null=True)
    Doc2image = models.ImageField(upload_to="img", null=True)
    Doc3image = models.ImageField(upload_to="img", null=True)
    Doc4image = models.ImageField(upload_to="img", null=True)
    Doc5image = models.ImageField(upload_to="img", null=True)
    intfield1 = models.IntegerField(null=True)
    intfield2 = models.IntegerField(null=True)
    intfield3 = models.IntegerField(null=True)
    intfield4 = models.IntegerField(null=True)
    intfield5 = models.IntegerField(null=True)
    DateField1 = models.DateTimeField(null=True)
    DateField2 = models.DateTimeField(null=True)
    DateField3 = models.DateTimeField(null=True)
    DateField4 = models.DateTimeField(null=True)
    DateField5 = models.DateTimeField(null=True)
    Charfield1 = models.CharField(null=True, max_length=50)
    Charfield2 = models.CharField(null=True, max_length=50)
    Charfield3 = models.CharField(null=True, max_length=50)
    Charfield4 = models.CharField(null=True, max_length=50)
    Charfield5 = models.CharField(null=True, max_length=50)


    
class Customer_financial_Details(models.Model):
    LoanId = models.ForeignKey(KYCIDS,null=False,unique=True,on_delete=models.CASCADE)
    HouseType = models.CharField(max_length=100, default=None)
    LandInAcre = models.PositiveIntegerField(default=None)
    NumberofAnimals = models.PositiveIntegerField(default=None)
    PovertyLine = models.CharField(max_length=100 , default=None)
    BankName = models.CharField(max_length=100 , default=None)
    BankAccountNo = models.BigIntegerField(default=None)
    ConfirmBankAccountNo = models.BigIntegerField(default=None)
    BankIFSCCode = models.CharField(max_length=100 , default=None)
    ConfirmBankIFSCCode = models.CharField(max_length=100 , default=None)

class Customer_Loan_Details(models.Model):
    LoanId = models.ForeignKey(KYCIDS,null=False,unique=True,on_delete=models.CASCADE)
    BranchName = models.CharField(max_length=100 , default=None)
    CenterId = models.CharField(max_length=100 , default=None)
    ProductCategory = models.CharField(max_length=100 , default=None)
    CategoryType = models.CharField(max_length=100 , default=None)
    Product = models.CharField(max_length=100 , default=None)
    PurposeId = models.CharField(max_length=100 , default=None)
    LoanAmount = models.PositiveIntegerField(default=None)
    InterestRate = models.FloatField(default=None)
    RepayFrequency = models.FloatField(default=None)
    GroupName = models.CharField(max_length=100 , default=None)

class Customer_Co_Insurer_Details(models.Model):
    CoInsurerRelation = models.CharField(max_length=100 , default=None)
    CoInsurerName = models.CharField(max_length=100 , default=None)
    CoInsurerDOB = models.DateField()
    CoInsurerAge = models.PositiveIntegerField(default=None)
    KYCIDType = models.CharField(max_length=100 , default=None)
    KYCID = models.CharField(max_length=100 , default=None)
    CoOccupation = models.CharField(max_length=100 , default=None)
    RemarkComments = models.CharField(max_length=500 , default=None)



# approved data table start



class approved_KYCIDS(models.Model):
    Aadhaar = models.BigIntegerField(unique=True)
    VoterCard = models.CharField(unique=True, max_length=50)
    OtherKYCIdtype = models.CharField(null=True, max_length=50)
    OtherKYCId = models.CharField(null=True, max_length=50)
    loanId = models.BigIntegerField()
    customerId = models.BigIntegerField()
    Application_No = models.BigIntegerField()
    

class approved_Customer_Details(models.Model):
    LoanId = models.ForeignKey(KYCIDS,null=False,unique=True,on_delete=models.CASCADE)
    Aadhaar = models.BigIntegerField(unique=True)
    Custimage = models.ImageField(upload_to="img",default=None)
    Member_Aadhar_Card_front = models.ImageField(upload_to="img",default=None)
    Member_Aadhar_Card_back = models.ImageField(upload_to="img",default=None)
    Member_Voter_Card_front = models.ImageField(upload_to="img",default=None)
    Member_Voter_Card_back = models.ImageField(upload_to="img",default=None)
    Member_Bank_Details = models.ImageField(upload_to="img",default=None)
    Member_Relationship_Proof = models.ImageField(upload_to="img",default=None)
    FirstName = models.CharField(max_length=100 , default=None)
    LastName = models.CharField(max_length=100 , default=None)
    Gender = models.CharField(max_length=100 , default=None)
    DateOfBirth = models.DateField()
    Age = models.IntegerField(default=None)
    MaritalStatus = models.CharField(max_length=100 , default=None)
    FSName = models.CharField(max_length=100 , default=None)
    FSType = models.CharField(max_length=100 , default=None)
    FSDateOfBirth = models.DateField()
    FSAdhaar = models.BigIntegerField(unique=True , default=None)
    MothersName = models.CharField(max_length=100 , default=None)
    Caste = models.CharField(max_length=100 , default=None)
    Religion = models.CharField(max_length=100 , default=None)
    Qualification = models.CharField(max_length=100 , default=None)
    Occupation = models.CharField(max_length=100 , default=None)
    PhoneNumber = models.BigIntegerField(default=None)
    AddressLine1 = models.CharField(max_length=100 , default=None)
    AddressLine2 = models.CharField(max_length=100 , default=None)
    AddressLine3 = models.CharField(max_length=100 , default=None)
    PreferredLanguage = models.CharField(max_length=100 , default=None)
    Pincode = models.PositiveIntegerField(default=None)
    Village = models.CharField(max_length=100 , default=None)
    State = models.CharField(max_length=100 , default=None, choices=STATE_CHOICES)
    District = models.CharField(max_length=100,default=None, choices=District_CHOICES)
    confirmAddressLine1 = models.CharField(max_length=100  , default=None)
    confirmAddressLine2 = models.CharField(max_length=100 , default=None)
    confirmAddressLine3 = models.CharField(max_length=100 , default=None)
    confirmPincode = models.IntegerField(default=None)
    confirmVillage = models.CharField(max_length=100 , default=None)
    confirmState = models.CharField(max_length=100, choices=STATE_CHOICES , default=None)
    confirmDistrict = models.CharField(
        max_length=100, choices=District_CHOICES , default=None
    )
    Doc1image = models.ImageField(upload_to="img", null=True)
    Doc2image = models.ImageField(upload_to="img", null=True)
    Doc3image = models.ImageField(upload_to="img", null=True)
    Doc4image = models.ImageField(upload_to="img", null=True)
    Doc5image = models.ImageField(upload_to="img", null=True)
    intfield1 = models.IntegerField(null=True)
    intfield2 = models.IntegerField(null=True)
    intfield3 = models.IntegerField(null=True)
    intfield4 = models.IntegerField(null=True)
    intfield5 = models.IntegerField(null=True)
    DateField1 = models.DateTimeField(null=True)
    DateField2 = models.DateTimeField(null=True)
    DateField3 = models.DateTimeField(null=True)
    DateField4 = models.DateTimeField(null=True)
    DateField5 = models.DateTimeField(null=True)
    Charfield1 = models.CharField(null=True, max_length=50)
    Charfield2 = models.CharField(null=True, max_length=50)
    Charfield3 = models.CharField(null=True, max_length=50)
    Charfield4 = models.CharField(null=True, max_length=50)
    Charfield5 = models.CharField(null=True, max_length=50)


    
class approved_Customer_financial_Details(models.Model):
    LoanId = models.ForeignKey(KYCIDS,null=False,unique=True,on_delete=models.CASCADE)
    HouseType = models.CharField(max_length=100, default=None)
    LandInAcre = models.PositiveIntegerField(default=None)
    NumberofAnimals = models.PositiveIntegerField(default=None)
    PovertyLine = models.CharField(max_length=100 , default=None)
    BankName = models.CharField(max_length=100 , default=None)
    BankAccountNo = models.BigIntegerField(default=None)
    ConfirmBankAccountNo = models.BigIntegerField(default=None)
    BankIFSCCode = models.CharField(max_length=100 , default=None)
    ConfirmBankIFSCCode = models.CharField(max_length=100 , default=None)

class approved_Customer_Loan_Details(models.Model):
    LoanId = models.ForeignKey(KYCIDS,null=False,unique=True,on_delete=models.CASCADE)
    BranchName = models.CharField(max_length=100 , default=None)
    CenterId = models.CharField(max_length=100 , default=None)
    ProductCategory = models.CharField(max_length=100 , default=None)
    CategoryType = models.CharField(max_length=100 , default=None)
    Product = models.CharField(max_length=100 , default=None)
    PurposeId = models.CharField(max_length=100 , default=None)
    LoanAmount = models.PositiveIntegerField(default=None)
    InterestRate = models.FloatField(default=None)
    RepayFrequency = models.FloatField(default=None)
    GroupName = models.CharField(max_length=100 , default=None)

class approved_Customer_Co_Insurer_Details(models.Model):
    CoInsurerRelation = models.CharField(max_length=100 , default=None)
    CoInsurerName = models.CharField(max_length=100 , default=None)
    CoInsurerDOB = models.DateField()
    CoInsurerAge = models.PositiveIntegerField(default=None)
    KYCIDType = models.CharField(max_length=100 , default=None)
    KYCID = models.CharField(max_length=100 , default=None)
    CoOccupation = models.CharField(max_length=100 , default=None)
    RemarkComments = models.CharField(max_length=500 , default=None)

# approved data table end





# rejected data table start



class rejected_KYCIDS(models.Model):
    Aadhaar = models.BigIntegerField(unique=True)
    VoterCard = models.CharField(unique=True, max_length=50)
    OtherKYCIdtype = models.CharField(null=True, max_length=50)
    OtherKYCId = models.CharField(null=True, max_length=50)
    loanId = models.BigIntegerField()
    customerId = models.BigIntegerField()
    Application_No = models.BigIntegerField()
    

class rejected_Customer_Details(models.Model):
    LoanId = models.ForeignKey(KYCIDS,null=False,unique=True,on_delete=models.CASCADE)
    Aadhaar = models.BigIntegerField(unique=True)
    Custimage = models.ImageField(upload_to="img",default=None)
    Member_Aadhar_Card_front = models.ImageField(upload_to="img",default=None)
    Member_Aadhar_Card_back = models.ImageField(upload_to="img",default=None)
    Member_Voter_Card_front = models.ImageField(upload_to="img",default=None)
    Member_Voter_Card_back = models.ImageField(upload_to="img",default=None)
    Member_Bank_Details = models.ImageField(upload_to="img",default=None)
    Member_Relationship_Proof = models.ImageField(upload_to="img",default=None)
    FirstName = models.CharField(max_length=100 , default=None)
    LastName = models.CharField(max_length=100 , default=None)
    Gender = models.CharField(max_length=100 , default=None)
    DateOfBirth = models.DateField()
    Age = models.IntegerField(default=None)
    MaritalStatus = models.CharField(max_length=100 , default=None)
    FSName = models.CharField(max_length=100 , default=None)
    FSType = models.CharField(max_length=100 , default=None)
    FSDateOfBirth = models.DateField()
    FSAdhaar = models.BigIntegerField(unique=True , default=None)
    MothersName = models.CharField(max_length=100 , default=None)
    Caste = models.CharField(max_length=100 , default=None)
    Religion = models.CharField(max_length=100 , default=None)
    Qualification = models.CharField(max_length=100 , default=None)
    Occupation = models.CharField(max_length=100 , default=None)
    PhoneNumber = models.BigIntegerField(default=None)
    AddressLine1 = models.CharField(max_length=100 , default=None)
    AddressLine2 = models.CharField(max_length=100 , default=None)
    AddressLine3 = models.CharField(max_length=100 , default=None)
    PreferredLanguage = models.CharField(max_length=100 , default=None)
    Pincode = models.PositiveIntegerField(default=None)
    Village = models.CharField(max_length=100 , default=None)
    State = models.CharField(max_length=100 , default=None, choices=STATE_CHOICES)
    District = models.CharField(max_length=100,default=None, choices=District_CHOICES)
    confirmAddressLine1 = models.CharField(max_length=100  , default=None)
    confirmAddressLine2 = models.CharField(max_length=100 , default=None)
    confirmAddressLine3 = models.CharField(max_length=100 , default=None)
    confirmPincode = models.IntegerField(default=None)
    confirmVillage = models.CharField(max_length=100 , default=None)
    confirmState = models.CharField(max_length=100, choices=STATE_CHOICES , default=None)
    confirmDistrict = models.CharField(
        max_length=100, choices=District_CHOICES , default=None
    )
    Doc1image = models.ImageField(upload_to="img", null=True)
    Doc2image = models.ImageField(upload_to="img", null=True)
    Doc3image = models.ImageField(upload_to="img", null=True)
    Doc4image = models.ImageField(upload_to="img", null=True)
    Doc5image = models.ImageField(upload_to="img", null=True)
    intfield1 = models.IntegerField(null=True)
    intfield2 = models.IntegerField(null=True)
    intfield3 = models.IntegerField(null=True)
    intfield4 = models.IntegerField(null=True)
    intfield5 = models.IntegerField(null=True)
    DateField1 = models.DateTimeField(null=True)
    DateField2 = models.DateTimeField(null=True)
    DateField3 = models.DateTimeField(null=True)
    DateField4 = models.DateTimeField(null=True)
    DateField5 = models.DateTimeField(null=True)
    Charfield1 = models.CharField(null=True, max_length=50)
    Charfield2 = models.CharField(null=True, max_length=50)
    Charfield3 = models.CharField(null=True, max_length=50)
    Charfield4 = models.CharField(null=True, max_length=50)
    Charfield5 = models.CharField(null=True, max_length=50)


    
class rejected_Customer_financial_Details(models.Model):
    LoanId = models.ForeignKey(KYCIDS,null=False,unique=True,on_delete=models.CASCADE)
    HouseType = models.CharField(max_length=100, default=None)
    LandInAcre = models.PositiveIntegerField(default=None)
    NumberofAnimals = models.PositiveIntegerField(default=None)
    PovertyLine = models.CharField(max_length=100 , default=None)
    BankName = models.CharField(max_length=100 , default=None)
    BankAccountNo = models.BigIntegerField(default=None)
    ConfirmBankAccountNo = models.BigIntegerField(default=None)
    BankIFSCCode = models.CharField(max_length=100 , default=None)
    ConfirmBankIFSCCode = models.CharField(max_length=100 , default=None)

class rejected_Customer_Loan_Details(models.Model):
    LoanId = models.ForeignKey(KYCIDS,null=False,unique=True,on_delete=models.CASCADE)
    BranchName = models.CharField(max_length=100 , default=None)
    CenterId = models.CharField(max_length=100 , default=None)
    ProductCategory = models.CharField(max_length=100 , default=None)
    CategoryType = models.CharField(max_length=100 , default=None)
    Product = models.CharField(max_length=100 , default=None)
    PurposeId = models.CharField(max_length=100 , default=None)
    LoanAmount = models.PositiveIntegerField(default=None)
    InterestRate = models.FloatField(default=None)
    RepayFrequency = models.FloatField(default=None)
    GroupName = models.CharField(max_length=100 , default=None)

class rejected_Customer_Co_Insurer_Details(models.Model):
    CoInsurerRelation = models.CharField(max_length=100 , default=None)
    CoInsurerName = models.CharField(max_length=100 , default=None)
    CoInsurerDOB = models.DateField()
    CoInsurerAge = models.PositiveIntegerField(default=None)
    KYCIDType = models.CharField(max_length=100 , default=None)
    KYCID = models.CharField(max_length=100 , default=None)
    CoOccupation = models.CharField(max_length=100 , default=None)
    RemarkComments = models.CharField(max_length=500 , default=None)

# rejected data table end


