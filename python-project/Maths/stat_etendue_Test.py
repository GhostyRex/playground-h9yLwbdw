#Ne pas oublier de changer le module à importer
from stat_etendue import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
([1,2,3,4],3),\
([2,4,1,3],3),\
([5,5,5,5,5,5,5],0),\
([8206, 211, 4957, 3355, 1110, 4179, 5378, 7741, 5364, 2229, 425, 8328, 7494, 8148, 6026, 7950, 1474, 2136, 8649, 2043, 4888, 1511, 6116, 7462, 4626, 3788, 9146, 3035, 6271, 1194, 9459, 6600, 9704, 9472, 659, 9427, 1699, 1975, 2172, 4347, 7795, 8703, 5394, 8376, 9984, 5711, 3595, 1802, 6575, 3969, 1077, 1373, 2174, 3248, 3049, 598, 8527, 9645, 3853, 7121, 7444, 5890, 6858, 1488, 3771, 6874, 7908, 9379, 8103, 6687, 4613, 8783, 9096, 9951, 9327, 6354, 561, 5034, 4243, 6698, 8287, 2891, 5172, 1811, 1154, 4748, 3135, 8565, 8061, 8548, 1593, 4740, 7779, 5572, 3926, 1136, 424, 9872, 5587, 4695, 6363, 6900, 4082, 1424, 9188, 2522, 791, 9208, 62, 3929, 3655, 5286, 6498, 5526, 9971, 9063, 8843, 1444, 8656, 4154, 9849, 9002, 78, 9065, 294, 5316, 1915, 1524, 6347, 4155, 6958, 4122, 5716, 896, 9930, 3693, 7442, 280, 8410, 1420, 3894, 5860, 8221, 873, 6408, 647, 2933, 4228, 6929, 8312, 2335, 2133, 3363, 6126, 2303, 8381, 8796, 4823, 7840, 9606, 7248, 1228, 2027, 190, 8489, 9220, 1170, 9114, 3872, 5482, 6622, 8953, 1208, 3537, 8082, 3352, 5527, 3276, 4525, 2861, 7531, 1947, 261, 6417, 548, 1723, 8620, 4851, 2637, 1591, 1627, 3965, 4801, 4207, 5992, 2412, 5278, 3882, 4009, 3579, 5101, 2285, 1170, 5964, 6235, 6121, 6129, 8944, 8832, 2933, 2315, 669, 9015, 9975, 5466, 8556, 7857, 1361, 6233, 9024, 388, 201, 232, 3842, 2704, 9707, 8546, 3142, 3112, 5910, 9044, 5478, 4010, 495, 6840, 7497, 1006, 6865, 3144, 8461, 6009, 2758, 1403, 1515, 252, 9763, 7422, 9229, 4297, 3358, 6133, 8757, 1561, 5627, 6596, 5356, 2805, 9265, 7061, 3798, 1112, 2851, 6486, 5971, 4003, 3049, 3421, 8296, 1419, 170, 8759, 5970, 9350, 7218, 3403, 9660, 7189, 3066, 6402, 4149, 797, 6949, 7369, 6179, 931, 7131, 960, 9829, 9882, 9724, 7933, 7089, 953, 1226, 1039, 4419, 5577, 227, 2803, 1335, 2363, 119, 8476, 432, 5842, 7296, 9397, 3181, 2168, 5391, 5949, 8525, 6795, 3995, 609, 5068, 4644, 110, 6419, 9230, 8271, 7278, 3596, 3323, 6305, 2200, 4016, 6271, 8453, 1132, 6021, 3947, 8926, 7325, 9984, 5437, 6314, 8245, 3745, 9713, 4736, 3160, 5245, 9603, 2259, 9437, 2947, 5752, 8482, 6626, 4104, 1733, 6881, 8734, 5939, 6532, 6492, 7122, 6767, 1961, 2661, 1031, 1463, 7004, 1415, 2373, 9831, 5909, 3745, 1950, 2356, 3845, 8524, 2764, 8321, 3685, 9351, 502, 4322, 2892, 5654, 3630, 5669, 8912, 5905, 4336, 5254, 3681, 5291, 529, 4148, 4297, 3634, 732, 9165, 5224, 180, 1268, 2427, 6006, 2631, 1236, 1667, 2104, 4982, 4331, 3046, 6649, 4862, 7437, 7012, 3922, 357, 861, 3943, 3402, 6209, 2438, 4982, 5917, 6817, 2902, 5667, 4414, 3325, 5899, 8991, 5669, 8397, 8339, 6992, 6307, 267, 5420, 7228, 2491, 2866, 5708, 3430, 8280, 6102, 8495, 2128, 6714, 4884, 7768, 3921, 7802, 3854, 3004, 744, 419, 9942, 939, 7625, 620, 1440, 3666, 6106, 2126, 366, 6712, 2503, 6370, 1530, 9964, 2369, 1244, 2690, 5754, 1217, 9116, 7035, 4267, 2685, 7381, 4159, 2279, 2892, 3652, 5000, 1299, 1195, 5501, 4334, 788, 5673, 6064, 9033, 9404, 1393, 9522, 806, 6054, 8666, 3566, 3617, 501, 5407, 175],9922)\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp,outp in input_output:
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        mon_programme(inp)
        count1 = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        assert str(count1) == str(outp), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()