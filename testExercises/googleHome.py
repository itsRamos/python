"""Practice Interview
This program creates an automated validation for the functionality of Google Home 
(Stub python code)

Author: Erick Ramos
Github: @itsRamos
Date: August 8, 2018
"""
import unittest



class GoogleHomeSpeaker(object):
    """Represents the state of a Google Home after a full power cycle.
    
    All the Google Home components are reset to default values
    """
    def __init__(self):
        self.POWER_ON = True
        self.INTERNET_CONNECTION = True
        self.MICROPHONE_STATUS = True
        self.MICROHPONE_SENSITIVITY = 0
        self.SPEAKER_STATUS = True
        self.SPEAKER_VOLUME = 0

        self.VOICE_ENCODER_STATUS = True
        self.VOICE_DECODER_STATUS = True
        
        self.SERVER_CONNECTION = False
    
        self.CHARGE_STATUS = None
        
    def isRegisterPoweredOn(self):
        return self.POWER_ON
    
    def powerOnRegister(self):
        self.POWER_ON = True
        return self.POWER_ON
        
    def isNumericKeyboardConnected(self):
        return self.KEYBOARD_STATUS
        
    def connectNumericKeyboard(self):
        self.KEYBOARD_STATUS = True
        return self.KEYBOARD_STATUS

    def isUIDisplayConnected(self):
        return self.DISPLAY_STATUS
        
    def connectUIDisplay(self):
        self.DISPLAY_STATUS = True
        return self.DISPLAY_STATUS
        
    def serverConnectionStatus(self):
        return self.CREDIT_CARD_SERVER_STATUS

    def reportChargeStatus(self):
        return self.CHARGE_STATUS

    def getSaleAmount(self):
        return self.SALE_AMOUNT
        
    def getCreditCardNumber(self):
        return self.CREDIT_CARD_NUMBER


class Functionality(GoogleHomeSpeaker):
    """Represents the functionaliy of a Sale Register Machine based on factory reset defaults.
    
    All functional aspects of the Sale Register Machine to automate the validation are described
    """
    def __init__(self):
        pass
        
    def getCreditCardNumber(self):
        raise NotImplementedError("STUB: progress in progress...")
    
    def isValidInput(self):
        raise NotImplementedError("STUB: progress in progress...")
        
    def submitSale(self):
        raise NotImplementedError("STUB: progress in progress...")
        
    def connectToCreditCardServer(self):
        raise NotImplementedError("STUB: progress in progress...")
        
    def disconnectFromCreditCardServer(self):
        raise NotImplementedError("STUB: progress in progress...")
        
    def reportChargeStatus(self):
        raise NotImplementedError("STUB: progress in progress...")
    
    
    
class AutomatedValidation(unittest.TestCase):
    """Represents the base automated validation for the functionality of the Sale Register Machine.
    
    Test fixtures are based on the built-in unit test library for Python    
    """
    @classmethod
    def setUpClass(cls):
        cls.REGISTER_MACHINE = Functionality()
        return cls.REGISTER_MACHINE
        
    @staticmethod
    def submitSaleInMachine(self):
        MACHINE_INPUT = Functionality.isValidInput
        SALE_SUBMISSION = Functionality.submitSale(MACHINE_INPUT)
        return SALE_SUBMISSION
        
        
        
class SalesPersonSubmitsSale(AutomatedValidation):
    """Represents the Test Case for the Sales person submitting a sale."""
    
    def test_valid_sale_is_submitted(self):
        VALID_SALE_SUBMISSION = AutomatedValidation().submitSaleInMachine
        self.assertTrue(VALID_SALE_SUBMISSION)
        
    def test_invalid_sale_is_submitted(self):
        INVALID_SALE_SUBMISSION = AutomatedValidation().submitSaleInMachine
        self.assertTrue(INVALID_SALE_SUBMISSION)
        
    def test_valid_sale_is_submitted_after_several_invalid(self):
        INVALID_SALE_SUBMISSION = AutomatedValidation().submitSaleInMachine
        INVALID_SALE_SUBMISSION = AutomatedValidation().submitSaleInMachine
        SALE_SUBMISSION = AutomatedValidation().submitSaleInMachine
        self.assertTrue(SALE_SUBMISSION)
        
    def test_valid_sale_is_submitted_and_interrupted(self):
        VALID_SALE_SUBMISSION = AutomatedValidation().submitSaleInMachine
        Functionality.disconnectFromCreditCardServer
        self.assertTrue(VALID_SALE_SUBMISSION)
        
        
        
class RegisterMachineConnectsToServer(AutomatedValidation):
    """Represents the Test Case for the Sales Register Machine connecting to the credit card server."""
        
    def test_register_machine_connects_to_online_server(self):
        SERVER_CONNECTION = Functionality.serverConnectionStatus
        if (SERVER_CONNECTION == False):
            Functionality.connectToCreditCardServer
            self.assertTrue(SERVER_CONNECTION)   
            
    def test_register_machine_connects_to_offline_server(self):
        SERVER_CONNECTION = Functionality.serverConnectionStatus
        if (SERVER_CONNECTION == True):
            Functionality.disconnectFromCreditCardServer
            self.assertFalse(SERVER_CONNECTION)  
            
    def test_connection_lost_during_transmission(self):
        SERVER_CONNECTION = Functionality.serverConnectionStatus
        if (SERVER_CONNECTION == True):
            Functionality.disconnectFromCreditCardServer
            self.assertFalse(SERVER_CONNECTION)  



class RegisterReportsTransactionStatus(AutomatedValidation):
    """Represents the Test Case for the Sales Register Machine reporting the states of transactions."""
        
    def test_valid_transactions_are_reported(self):
        VALID_REPORT = Functionality.reportChargeStatus
        self.assertTrue(VALID_REPORT)   
            
    def test_invalid_transactions_are_reported(self):
        INVALID_REPORT = Functionality.reportChargeStatus
        self.assertTrue(INVALID_REPORT)  
            
            
            
class SaleAmountInputThroughNumericKeypad(AutomatedValidation):
    """Represents the Test Case for the sale amount being input into the Sales Register Machine."""
        
    def test_valid_sale_amount_is_input(self):
        VALID_SALE_AMOUNT = Functionality.getSaleAmount
        self.assertNotEqual(VALID_SALE_AMOUNT, 1)   
            
    def test_invalid_sale_amount_is_input(self):
        INVALID_SALE_AMOUNT = Functionality.getSaleAmount
        self.assertNotEqual(INVALID_SALE_AMOUNT, 0)   
      
      
      
class CreditCardInformationInput(AutomatedValidation):
    """Represents the Test Case for the credit card information input into the Sales Register Machine."""
        
    def test_valid_credit_card_info_is_input(self):
        VALID_CREDIT_CARD = Functionality.getCreditCardNumber
        self.assertTrue(VALID_CREDIT_CARD)   
            
    def test_invalid_credit_card_info_is_input(self):
        INVALID_CREDIT_CARD = Functionality.getCreditCardNumber
        self.assertTrue(INVALID_CREDIT_CARD)
    
            
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
