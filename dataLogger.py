import csv


class data_logger():


    def twoPressurTransducers(self, data, iteration, fileName='youForgotToNameYourFile',
                           save_path='C:/Users/bob/Desktop/imu_presure/tests/test_files/'):

        fileName = fileName + '.csv'
        nameOfFile = save_path + fileName

        if iteration == 0:
            with open(nameOfFile, "w") as csvfile:
                fieldnames = ['Voltage_P0', 'Voltage_N0', 'Pressure0',
                              'Voltage_P1', 'Voltage_N1', 'Pressure1']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'Voltage_P0': data[0], 'Voltage_N0': data[1], 'Pressure0': data[2],
                                 'Voltage_P1': data[3], 'Voltage_N1': data[4], 'Pressure1': data[5]})

        if iteration != 0:
            with open(nameOfFile, "a") as csvfile:
                fieldnames = ['Voltage_P0', 'Voltage_N0', 'Pressure0',
                              'Voltage_P1', 'Voltage_N1', 'Pressure1']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'Voltage_P0': data[0], 'Voltage_N0': data[1], 'Pressure0': data[2],
                                 'Voltage_P1': data[3], 'Voltage_N1': data[4], 'Pressure1': data[5]})



    def a3_g3_t2(self, data, iteration, fileName='youForgotToNameYourFile',
                           save_path='C:/Users/bob/Desktop/imu_presure/tests/test_files/'):

        fileName = fileName + '.csv'
        nameOfFile = save_path + fileName
        fieldnames = ['xAcc', 'yAcc', 'zAcc',
                      'xGyr', 'yGyr', 'zGyr',
                      'vp0', 'vn0', 'p0',
                      'vp1', 'vn1', 'p1',
                      'datetime']


        if iteration == 0:
            with open(nameOfFile, "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'xAcc': data[0], 'yAcc': data[1], 'zAcc': data[2],
                                 'xGyr': data[3], 'yGyr': data[4], 'zGyr': data[5],
                                 'vp0': data[6], 'vn0': data[7], 'p0': data[8],
                                 'vp1': data[9], 'vn1': data[10], 'p1': data[11],
                                 'datetime': data[12]})

        if iteration != 0:
            with open(nameOfFile, "a") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'xAcc': data[0], 'yAcc': data[1], 'zAcc': data[2],
                                 'xGyr': data[3], 'yGyr': data[4], 'zGyr': data[5],
                                 'vp0': data[6], 'vn0': data[7], 'p0': data[8],
                                 'vp1': data[9], 'vn1': data[10], 'p1': data[11],
                                 'datetime': data[12]})




    def tca3_r_t2(self, data, iteration, fileName='youForgotToNameYourFile',
                           save_path='C:/Users/bob/Desktop/imu_presure/tests/test_files/'):

        fileName = fileName + '.csv'
        nameOfFile = save_path + fileName

        fieldnames = ['xAcc', 'yAcc', 'zAcc',
                      'R[00]', 'R[01]', 'R[02]',
                      'R[10]', 'R[11]', 'R[12]',
                      'R[20]', 'R[21]', 'R[22]',
                      'vp0', 'vn0', 'p0',
                      'vp1', 'vn1', 'p1',
                      'datetime']


        if iteration == 0:
            with open(nameOfFile, "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'xAcc': data[0], 'yAcc': data[1], 'zAcc': data[2],
                                 'R[00]': data[3], 'R[01]': data[4], 'R[02]': data[5],
                                 'R[10]': data[6], 'R[11]': data[7], 'R[12]': data[8],
                                 'R[20]': data[9], 'R[21]': data[10], 'R[22]': data[11],
                                 'vp0': data[12], 'vn0': data[13], 'p0': data[14],
                                 'vp1': data[15], 'vn1': data[16], 'p1': data[17],
                                 'datetime': data[18]})

        if iteration != 0:
            with open(nameOfFile, "a") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'xAcc': data[0], 'yAcc': data[1], 'zAcc': data[2],
                                 'R[00]': data[3], 'R[01]': data[4], 'R[02]': data[5],
                                 'R[10]': data[6], 'R[11]': data[7], 'R[12]': data[8],
                                 'R[20]': data[9], 'R[21]': data[10], 'R[22]': data[11],
                                 'vp0': data[12], 'vn0': data[13], 'p0': data[14],
                                 'vp1': data[15], 'vn1': data[16], 'p1': data[17],
                                 'datetime': data[18]})