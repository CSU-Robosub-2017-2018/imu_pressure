from context import imu_tools
from context import imu_base
from context import pressure_base
from context import data_logger
import datetime

# from imu_framework.tests.context import imu_no_thrd_9250


if __name__ == '__main__':

    ######## instantiate IMUs ####################################
    # myIMU_no_thrd_9250 = imu_no_thrd_9250()


    myIMU_base = imu_base()
    myPressure_base = pressure_base(0.042389869, -0.124235215, 100)



    ######## connect all IMUs #############################################
    # myIMU_no_thrd_9250.connect()

    myIMU_base.connect()
    myPressure_base.setUpChanel(fileName='pressure_base_data_2.csv')

    # fix me   take all and put into tools so multipal instantiations are can be achived
    ##########################################################################
    myTools = imu_tools(imu=myIMU_base)
    myDataLogger = data_logger()


    i = 0
    print('start')
    while i <= 4500:


        imu_data = myTools.get_arhs_tcAccel_R()
        # print(tcAcceleration_R)

        myPressure_base.set_data()
        voltageData = myPressure_base.getAllVoltageData()
        press_data = myPressure_base.get_pressure()

        time_now = datetime.datetime.now().strftime("%H:%M:%S")

        data = [imu_data[0], imu_data[1], imu_data[2],
                imu_data[3], imu_data[4], imu_data[5],
                imu_data[6], imu_data[7], imu_data[8],
                imu_data[9], imu_data[10], imu_data[11],
                voltageData[0], voltageData[1], press_data[0],
                voltageData[2], voltageData[3], press_data[1],
                time_now]

        print(data)
        myDataLogger.tca3_r_t2(data, i, 'test_tcAcell_R_2xPressur')

        i = i + 1

        ######## disconnect all IMUs #############################################

    print('end')