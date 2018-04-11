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

    # fix me   take all and put into tools so multiple instantiations are can be achieved
    ##########################################################################
    myTools = imu_tools(imu=myIMU_base)
    myDataLogger = data_logger()




    i = 0
    print('start')
    while i <= 4500:

        rawAccel = myTools.get_raw_scale_data()

        myPressure_base.set_data()
        voltageData = myPressure_base.getAllVoltageData()
        pressureData = myPressure_base.get_pressure()

        time_now = datetime.datetime.now().strftime("%H:%M:%S")

        data = [rawAccel[0], rawAccel[1], rawAccel[2],
                rawAccel[3], rawAccel[4], rawAccel[5],
                voltageData[0], voltageData[1], pressureData[0],
                voltageData[2], voltageData[3], pressureData[1],
                time_now]

        print(data)

        # myDataLogger.a3_g3_t2(data, i, 'test_data_logger')


        i = i + 1

        ######## disconnect all IMUs #############################################

    # myIMU_no_thrd_sparton.disconnect()
    print(i)