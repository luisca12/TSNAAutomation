import traceback
import os

def mkdir():
    path = "logs"
    # path1 = "Outputs"
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except Exception as Error:
            print(f"ERROR: Wasn't possible to create new folder \"{path}\"")
            print(traceback.format_exc())
    # if not os.path.exists(path1):
    #     try:
    #         os.mkdir(path1)
    #     except Exception as Error:
    #         print(f"ERROR: Wasn't possible to create new folder \"{path1}\"")
    #         print(traceback.format_exc())

def checkIsDigit(input_str):
    from log import authLog
    try:
        authLog.info(f"String successfully validated selection number {input_str}, from checkIsDigit function.")
        return input_str.strip().isdigit()
    
    except Exception as error:
        pass
        authLog.error(f"Invalid option chosen: {input_str}, error: {error}")
        authLog.error(traceback.format_exc())
