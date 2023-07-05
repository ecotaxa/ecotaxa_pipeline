


from pathlib import PurePath
import pandas as pd

from cytosenseModel import UlcoListmode, pulse


class mock_ulco_small_data():


    local_path = 'tests/cytosense/ULCO/mock_small_data'
    sample_name = 'R4_photos_flr16_2uls_10min 2022-09-14 12h28'
    pulse_filename = sample_name +  '_Pulses.csv'
    polynomial_filename = sample_name +  '_Polynomial_Pulses.csv'
    listmode_filename = sample_name +  '_Listmode.csv'
    info_filename = sample_name +  '_Infos.csv'

    
    pulse_model = pulse 
    ulco_listmode_model = UlcoListmode
    # cannot test, because model is not force to take all columns
    # del corrupted_model._mapping['object_id']

    data = {
            'raw_folder': PurePath(local_path),
            'sample_name': sample_name,
            'csv_pulse': {
                            'filename': polynomial_filename,
                            'mapping': pulse_model,
                            'path': PurePath(local_path , polynomial_filename),
                            'csv_configuration': {'decimal': ',', 'delimiter': ';'}
                        },
            'csv_listmode': {
                            'filename': listmode_filename,
                            'mapping': ulco_listmode_model,
                            'path': PurePath(local_path , listmode_filename),
                            'csv_configuration': {'decimal': ',', 'delimiter': ';'}
                        }
        }
    
    headerCSV = ["Particle ID","FWS_coef_0","FWS_coef_1","FWS_coef_2","FWS_coef_3","FWS_coef_4","FWS_coef_5","FWS_coef_6","FWS_coef_7","FWS_coef_8","FWS_coef_9","SWS_coef_0","SWS_coef_1","SWS_coef_2","SWS_coef_3","SWS_coef_4","SWS_coef_5","SWS_coef_6","SWS_coef_7","SWS_coef_8","SWS_coef_9","FL Yellow_coef_0","FL Yellow_coef_1","FL Yellow_coef_2","FL Yellow_coef_3","FL Yellow_coef_4","FL Yellow_coef_5","FL Yellow_coef_6","FL Yellow_coef_7","FL Yellow_coef_8","FL Yellow_coef_9","FL Orange_coef_0","FL Orange_coef_1","FL Orange_coef_2","FL Orange_coef_3","FL Orange_coef_4","FL Orange_coef_5","FL Orange_coef_6","FL Orange_coef_7","FL Orange_coef_8","FL Orange_coef_9","FL Red_coef_0","FL Red_coef_1","FL Red_coef_2","FL Red_coef_3","FL Red_coef_4","FL Red_coef_5","FL Red_coef_6","FL Red_coef_7","FL Red_coef_8","FL Red_coef_9","Curvature_coef_0","Curvature_coef_1","Curvature_coef_2","Curvature_coef_3","Curvature_coef_4","Curvature_coef_5","Curvature_coef_6","Curvature_coef_7","Curvature_coef_8","Curvature_coef_9"]

    header = [
        'object_id',  
        'object_coef_0_FWS', 'object_coef_1_FWS', 'object_coef_2_FWS', 'object_coef_3_FWS', 'object_coef_4_FWS', 'object_coef_5_FWS', 'object_coef_6_FWS', 'object_coef_7_FWS',  'object_coef_8_FWS', 'object_coef_9_FWS', 
        'object_coef_0_SWS', 'object_coef_1_SWS', 'object_coef_2_SWS', 'object_coef_3_SWS','object_coef_4_SWS', 'object_coef_5_SWS','object_coef_6_SWS', 'object_coef_7_SWS','object_coef_8_SWS', 'object_coef_9_SWS',
        'object_coef_0_FL_Yellow', 'object_coef_1_FL_Yellow', 'object_coef_2_FL_Yellow', 'object_coef_3_FL_Yellow','object_coef_4_FL_Yellow','object_coef_5_FL_Yellow',  'object_coef_6_FL_Yellow', 'object_coef_7_FL_Yellow', 'object_coef_8_FL_Yellow', 'object_coef_9_FL_Yellow',
        'object_coef_0_FL_Orange', 'object_coef_1_FL_Orange', 'object_coef_2_FL_Orange', 'object_coef_3_FL_Orange', 'object_coef_4_FL_Orange', 'object_coef_5_FL_Orange',  'object_coef_6_FL_Orange', 'object_coef_7_FL_Orange', 'object_coef_8_FL_Orange', 'object_coef_9_FL_Orange', 
        'object_coef_0_FL_Red', 'object_coef_1_FL_Red', 'object_coef_2_FL_Red', 'object_coef_3_FL_Red', 'object_coef_4_FL_Red', 'object_coef_5_FL_Red', 'object_coef_6_FL_Red',  'object_coef_7_FL_Red', 'object_coef_8_FL_Red', 'object_coef_9_FL_Red',
        'object_coef_0_curvature', 'object_coef_1_Curvature', 'object_coef_2_Curvature', 'object_coef_3_Curvature', 'object_coef_4_Curvature', 'object_coef_5_Curvature','object_coef_6_Curvature', 'object_coef_7_Curvature', 'object_coef_8_Curvature', 'object_coef_9_Curvature',
    ]    

    type_header=["[t]"]+["[f]" for _ in range(len(header)-1)]

    data_pulse = [
        [sample_name+"_0",-68.04754805517467,170.0141493931962,-103.1316447602405,29.596328167863966,-4.03996672486493,0.298463038013299,-0.012738856779690094,0.00031511120820561066,-4.202159571690249e-06,2.339972032248827e-08,-12.268580334705911,21.251139563742033,-11.216311216723625,2.6785118950851046,-0.31771238058569834,0.020995654211594085,-0.0008162421317762789,1.8621908198765924e-05,-2.311953790125044e-07,1.2075778859829984e-09,1.8811309009657804,-1.2156615289293073,0.6377312527859975,-0.14230439166742187,0.01690194501963563,-0.0011700045284822234,4.855372686315206e-05,-1.1880964728526058e-06,1.5794023326397032e-08,-8.794527414015224e-11,0.4787292001760408,0.41191530664708703,-0.39032631189160605,0.15185519167238415,-0.02258010551023266,0.001696587617100022,-7.189117237027885e-05,1.7502358824879186e-06,-2.2913650467506653e-08,1.2527475792832748e-10,-0.9894049579900819,3.506640470330078,-1.8784838030464424,0.5521080044545936,-0.07338391569421437,0.005145379667917397,-0.00020649175625426895,4.7922951465235416e-06,-6.002581061950583e-08,3.1477256589659894e-10,-0.04681117509893093,-0.14694233887777908,0.07206825782553343,-0.012868837037907121,0.001192081174480416,-6.41546738733492e-05,2.0753671106896203e-06,-3.961062419913173e-08,4.0843949179365186e-10,-1.7381832174903998e-12],
        [sample_name+"_1",160.19119195047253,-286.09868022470226,228.07354447238112,-86.03596463339086,18.455134518894557,-2.3036212782897127,0.16978010663557128,-0.007290442639826719,0.00016889041922082815,-1.6335019533570842e-06,6.626103715168874,-9.44110577054712,6.538832979567237,-1.9856579821497977,0.3223137936483027,-0.022238348036304638,-1.8894179822981794e-05,8.217072628400408e-05,-3.963450214115317e-06,5.965759246856086e-08,0.16956749225997858,1.1925702712165134,-0.9237935877185861,0.3618918438082599,-0.07652162162106012,0.009534501581088737,-0.0007215413579637583,3.2519417365950426e-05,-8.011369360075277e-07,8.29468422755171e-09,2.0399009287926013,-1.9785053921333366,1.6715046908722941,-0.6692789384943116,0.14595319141663113,-0.018040579583949407,0.0012996668295356235,-5.409511183562201e-05,1.2053390821597312e-06,-1.1117284013575295e-08,0.7735580495353407,2.1835146702123023,-1.597605147694461,0.6868033062165819,-0.14206108473251483,0.017674480352976668,-0.0014054329107636996,6.868073255908877e-05,-1.8511715003430167e-06,2.089945358638368e-08,0.01754952399380441,-0.12523873363563956,0.0533746850295197,-0.010144465106239266,0.0012436765698012847,-0.00012116008433596569,9.519033019646833e-06,-5.193997316121304e-07,1.624904230774717e-08,-2.1331706280896722e-10],
        [sample_name+"_2",96.81589626241993,-169.27122551281087,114.25624901934184,-35.34135583950736,5.997896015363872,-0.564085617503418,0.0297274224133677,-0.0008547403579370158,1.1955083552100815e-05,-5.615256002146967e-08,3.2277515255547016,-4.021300770204839,2.2953581741097624,-0.4850386326347379,0.021759456220065483,0.007859107889356575,-0.0012486843174860625,7.533431478517207e-05,-2.088108511332875e-06,2.219683936981322e-08,0.6927224256293694,-0.12959628233737353,-0.03917707288512781,0.07653999462176653,-0.026021223564060746,0.004073670293733698,-0.0003410911202399483,1.5742844476525992e-05,-3.7805124575447775e-07,3.6933881342950844e-09,2.4157010869567985,-3.9253995404023434,2.8656958350431934,-0.9937021433235225,0.18835546875779802,-0.0203882553012097,0.0012978091640555472,-4.817689383465123e-05,9.666647179057516e-07,-8.111194334384088e-09,2.1254757818464682,-2.1875842946068262,1.4000299788403117,-0.35583447313132,0.06125278986919644,-0.006037758094735724,0.0003223053143248557,-8.888260271603064e-06,1.0660629482128864e-07,-2.4338463282950166e-10,0.16844666990846663,-0.16111268233201206,0.03629640611142444,-0.003762431821941539,0.0003356107589018647,-3.839439476747628e-05,3.3878169981765115e-06,-1.7221985513032618e-07,4.541360061283899e-09,-4.850420149805663e-11],
        [sample_name+"_3",87.25124613003015,-165.5859542186256,127.68193388761091,-46.102817041994484,9.357272260376913,-1.0761961934763686,0.07106343218363267,-0.0026523274938349338,5.142060591542531e-05,-3.9412455525837384e-07,-0.098479876163033,2.2469525881586074,-2.3215307272601846,1.229352264621881,-0.35356840009827784,0.060950902819874433,-0.006046194677343353,0.0003348673127234852,-9.63059291156446e-06,1.1221068100366737e-07,0.1891498452011504,0.8984546624861437,-0.7634007953689952,0.30625912749063927,-0.06782961038208167,0.008833847255355513,-0.0006883333149939859,3.1467115352796395e-05,-7.77500384847609e-07,8.011591646857876e-09,1.792964396284817,-2.3523444874640718,1.788334626367846,-0.6332436389193469,0.12347123562286666,-0.013843800183896707,0.0009139074052585819,-3.510005888868798e-05,7.253899157356212e-07,-6.230775390839122e-09,1.0672577399377818,-0.30662018316772044,0.2768571354020154,-0.07737514724622882,0.018377412825638744,-0.0013063324021242101,-6.999075999945464e-05,1.2961020916715635e-05,-5.749332358076772e-07,8.522532321643362e-09,0.39808215170278327,-0.45393536457761074,0.18098914395310775,-0.040748727996311074,0.0060227021435502615,-0.0006084078188255376,4.145115661209652e-05,-1.8106920296291622e-06,4.5520709778778296e-08,-4.977209131010229e-10],
        [sample_name+"_29",167.63803182075088,-285.13913950946034,163.48557806082334,-43.58269059022846,6.247198208117836,-0.5020004412717721,0.023362250972442856,-0.0006266543702649454,9.004175321666755e-06,-5.3722448873497215e-08,8.758454457447314,-13.741044694641564,7.780776420645863,-2.0258206233890106,0.27399573541710764,-0.020139877517058785,0.0008340084952403479,-1.9289952875520287e-05,2.2881045300599347e-07,-1.0506892055226045e-09,0.7630973926342697,-0.42964110885791196,0.22186511944778337,-0.048121940127435425,0.004367494987886956,-7.239367141692905e-05,-1.2511317992711592e-05,8.335643990503596e-07,-2.0186244507019104e-08,1.7623059340300567e-10,2.29384374415565,-2.8366046197368577,1.7851808898119526,-0.5351601567868325,0.08473186467723226,-0.007250366222782847,0.0003513200411885568,-9.697294626894115e-06,1.425506417034541e-07,-8.678552453892432e-10,1.4044218923793963,-1.5206088864767824,1.023030774761746,-0.39930990694197366,0.08480800398566561,-0.00817793499044534,0.00040425669716958516,-1.0721023307439035e-05,1.4467732061901095e-07,-7.732094578250166e-10,0.7090471197445706,-0.04734871821790856,-0.1258835308401218,0.039303908689241634,-0.005397323566360818,0.0004162341129207915,-1.9243945756555243e-05,5.300061547395002e-07,-8.02378630175771e-09,5.142858169920372e-11],
        [sample_name+"_3269",199.379570374963,-295.842360665635,140.19659307842613,-30.0190594174841,3.353557848906983,-0.2079933736315469,0.007428290199580921,-0.0001517932218032946,1.6444753076721615e-06,-7.292717948317964e-09,47.06234259392744,-67.63908118822174,31.82129602740207,-6.678634255263537,0.7076082326480992,-0.03862374223088996,0.0010909314067093319,-1.4327688405124872e-05,4.2836112147451035e-08,4.6173346173509475e-10,3.5018717351283275,-4.246933446075114,2.0079303687443386,-0.43235189190472423,0.0486610871194474,-0.0030113418338406153,0.00010630987117339006,-2.1305043424318793e-06,2.2461768685413656e-08,-9.603481619900653e-11,12.513117269853055,-18.998455611388966,9.797203954313552,-2.3129030284254313,0.28527781738059,-0.019422084876482892,0.000761345431277292,-1.7177798571858748e-05,2.077568228439444e-07,-1.0452522156669114e-09,43.72201104412085,-64.27137551597012,31.497753171893617,-7.086720593219816,0.8396640441710989,-0.05481033199464663,0.002049132142050755,-4.381371566452414e-05,4.986776925578978e-07,-2.3430520469086337e-09,0.1376695640924506,0.5209526461397347,-0.2385296630717405,0.04209032835952636,-0.003885611355464286,0.00020822133637437917,-6.710668386967188e-06,1.2810666534947057e-07,-1.3315443038903759e-09,5.786060647658829e-12],
        [sample_name+"_3543",37.847569090516345,-29.340105497158753,10.712732563350352,-1.9102841421941048,0.18748999275343342,-0.008999542077002121,0.00022862098960593617,-3.173048105037512e-06,2.2790784858371306e-08,-6.628971577584796e-11,-74.6667578620079,234.57362076284835,-71.71795706971744,9.390308562417065,-0.6245154365728449,0.023932231683686668,-0.0005508270382330387,7.494325720626853e-06,-5.5394856898160856e-08,1.7110262962592224e-10,-1.4824618790619795,1.9332217787637243,-0.3911956108841608,0.017468048033809917,0.001815983321124831,-0.000167930706912399,5.500898648033854e-06,-9.00542191229958e-08,7.454073745464397e-10,-2.4991900109418458e-12,-5.108823769568062,6.855689305486504,-2.0011201039875655,0.2037672913210812,-0.006288019171394909,4.8252682086761257e-05,1.2187490871461698e-07,1.8761745831639127e-08,-4.855625537927231e-10,2.987419856848487e-12,-27.3941805818514,32.56027571666022,-8.259119555103268,0.6861242720382932,-0.005800911657911928,-0.000906628525481631,3.265889362698931e-05,-4.4361914814518423e-07,2.453579088906172e-09,-3.3941069739216956e-12,-0.2737353841507535,0.11273130563935911,-0.03951827527260601,0.005640423745298455,-0.00040780572099579,1.6723897122812394e-05,-4.0586335864432183e-07,5.777638180609396e-09,-4.463052729154384e-11,1.4454904070134359e-13],
        [sample_name+"_4206",4.184095020222003,66.70123869227936,-23.722892814372173,3.4511100848986187,-0.1958399765478837,0.005537462968436103,-8.45999530273397e-05,6.896251590765643e-07,-2.649882443132145e-09,3.104573646300617e-12,80.08383883531188,-2.6994869368735954,1.7066064194498296,-0.29541996621926825,0.021494348461736736,-0.0008118053772317628,1.7324320763379463e-05,-2.110318971996032e-07,1.3697500646352577e-09,-3.67758677817544e-12,-0.5599543878771875,1.09174193886297,-0.3082130952388093,0.03542674363534289,-0.0019479298864734614,5.884427484164022e-05,-1.0355944163996354e-06,1.0606677969301862e-08,-5.871199395539507e-11,1.359987304123782e-13,1.504850036938418,-0.6290732560791779,0.06790282218864835,0.003981389907039526,-0.00024586602936311585,-2.416979879366261e-06,3.3485640983649725e-07,-7.2991358416571606e-09,6.555357671234982e-11,-2.1695209078049766e-13,-1.5943385030893467,4.630464630473345,-1.4708602797207706,0.20108220997980544,-0.010993551015975465,0.00029743602640290784,-4.2507755397668896e-06,3.068626580992862e-08,-8.690510837397552e-11,-1.2390670300540023e-14,0.10093478980377572,-0.073945481497039,0.01615877106066168,-0.001582094811447267,8.303946936429822e-05,-2.544861024953992e-06,4.699545988863857e-08,-5.151274771779635e-10,3.0870263524935436e-12,-7.79033542864106e-15],
        [sample_name+"_10104",353.4019785902075,-300.50931124670495,67.71309692164564,-6.3758394578206135,0.33132366891136916,-0.01046566725372772,0.00020679093809992325,-2.5013152435630283e-06,1.6928594519914215e-08,-4.901584089912509e-11,26.090913261916,-22.07568855758994,5.154580293526573,-0.4626215646533751,0.023941796919992604,-0.0008065653015955101,1.8016289634409706e-05,-2.5334784780286304e-07,1.9942623796099706e-09,-6.619596882806372e-12,4.951394564185177,-3.520267574814959,0.6675485216852344,-0.042865630759796644,0.0010165325415657477,5.203658381861246e-06,-7.275603612060069e-07,1.445114574440913e-08,-1.2318028457964825e-10,3.994020874205287e-13,21.30064543375171,-17.16480767701125,3.628977777248023,-0.28484484820816686,0.01088688348075027,-0.0002142850303209622,1.953507906776608e-06,-2.134279408179647e-09,-8.599981475889998e-11,4.2576628167386866e-13,81.64559528643373,-65.47911883286196,13.578212339050005,-1.0233017256433508,0.03610004176099255,-0.0005826251731129589,1.8055342389544937e-06,6.846950231792823e-08,-8.776414566590535e-10,3.247947434329225e-12,0.6664085145046472,0.14553228475715788,-0.08238443314215625,0.010964723844340715,-0.0007066894848787671,2.5727686836543392e-05,-5.556492080593385e-07,7.0567090820806274e-09,-4.868450681666122e-11,1.4079473222906686e-13]
    ]

   


    # header_listmode = ["Particle ID","Sample Length","Arrival Time","FWS Length","FWS Total","FWS Maximum","FWS Average","FWS Inertia","FWS Center of gravity","FWS Fill factor","FWS Asymmetry","FWS Number of cells","FWS First","FWS Last","FWS Minimum","FWS SWS covariance","SWS Length","SWS Total","SWS Maximum","SWS Average","SWS Inertia","SWS Center of gravity","SWS Fill factor","SWS Asymmetry","SWS Number of cells","SWS First","SWS Last","SWS Minimum","SWS SWS covariance","FL Yellow Length","FL Yellow Total","FL Yellow Maximum","FL Yellow Average","FL Yellow Inertia","FL Yellow Center of gravity","FL Yellow Fill factor","FL Yellow Asymmetry","FL Yellow Number of cells","FL Yellow First","FL Yellow Last","FL Yellow Minimum","FL Yellow SWS covariance","FL Orange Length","FL Orange Total","FL Orange Maximum","FL Orange Average","FL Orange Inertia","FL Orange Center of gravity","FL Orange Fill factor","FL Orange Asymmetry","FL Orange Number of cells","FL Orange First","FL Orange Last","FL Orange Minimum","FL Orange SWS covariance","FL Red Length","FL Red Total","FL Red Maximum","FL Red Average","FL Red Inertia","FL Red Center of gravity","FL Red Fill factor","FL Red Asymmetry","FL Red Number of cells","FL Red First","FL Red Last","FL Red Minimum","FL Red SWS covariance","Curvature Length","Curvature Total","Curvature Maximum","Curvature Average","Curvature Inertia","Curvature Center of gravity","Curvature Fill factor","Curvature Asymmetry","Curvature Number of cells","Curvature First","Curvature Last","Curvature Minimum","Curvature SWS covariance"]
    # header_listmode = ["Particle ID","Sample Length","Arrival Time","FWS Length","FWS Total","FWS Maximum","FWS Average","FWS Inertia","FWS Center of gravity","FWS Fill factor","FWS Asymmetry","FWS Number of cells","FWS First","FWS Last","FWS Minimum","FWS SWS covariance","SWS Length","SWS Total","SWS Maximum","SWS Average","SWS Inertia","SWS Center of gravity","SWS Fill factor","SWS Asymmetry","SWS Number of cells","SWS First","SWS Last","SWS Minimum","SWS SWS covariance","FL Yellow Length","FL Yellow Total","FL Yellow Maximum","FL Yellow Average","FL Yellow Inertia","FL Yellow Center of gravity","FL Yellow Fill factor","FL Yellow Asymmetry","FL Yellow Number of cells","FL Yellow First","FL Yellow Last","FL Yellow Minimum","FL Yellow SWS covariance","FL Orange Length","FL Orange Total","FL Orange Maximum","FL Orange Average","FL Orange Inertia","FL Orange Center of gravity","FL Orange Fill factor","FL Orange Asymmetry","FL Orange Number of cells","FL Orange First","FL Orange Last","FL Orange Minimum","FL Orange SWS covariance","FL Red Length","FL Red Total","FL Red Maximum","FL Red Average","FL Red Inertia","FL Red Center of gravity","FL Red Fill factor","FL Red Asymmetry","FL Red Number of cells","FL Red First","FL Red Last","FL Red Minimum","FL Red SWS covariance"]
    header_listmode = ["object_id","sample_id","sample_length","sample_arrival_time","object_fws_length","object_fws_total","object_fws_maximum","object_fws_average","object_fws_inertia","object_fws_center_of_gravity","object_fws_fill_factor","object_fws_asymmetry","object_fws_number_of_cells","object_fws_first","object_fws_last","object_fws_minimum","object_fws_sws_covariance","object_sidewards_scatter_length","object_sidewards_scatter_total","object_sidewards_scatter_maximum","object_sidewards_scatter_average","object_sidewards_scatter_inertia","object_sidewards_scatter_center_of_gravity","object_sidewards_scatter_fill_factor","object_sidewards_scatter_asymmetry","object_sidewards_scatter_number_of_cells","object_sidewards_scatter_first","object_sidewards_scatter_last","object_sidewards_scatter_minimum","object_sidewards_scatter_sws_covariance","object_fl_yellow_length","object_fl_yellow_total","object_fl_yellow_maximum","object_fl_yellow_average","object_fl_yellow_inertia","object_fl_yellow_center_of_gravity","object_fl_yellow_fill_factor","object_fl_yellow_asymmetry","object_fl_yellow_number_of_cells","object_fl_yellow_first","object_fl_yellow_last","object_fl_yellow_minimum","object_fl_yellow_sws_covariance","object_fl_orange_length","object_fl_orange_total","object_fl_orange_maximum","object_fl_orange_average","object_fl_orange_inertia","object_fl_orange_center_of_gravity","object_fl_orange_fill_factor","object_fl_orange_asymmetry","object_fl_orange_number_of_cells","object_fl_orange_first","object_fl_orange_last","object_fl_orange_minimum","object_fl_orange_sws_covariance","object_fl_red_length","object_fl_red_total","object_fl_red_maximum","object_fl_red_average","object_fl_red_inertia","object_fl_red_center_of_gravity","object_fl_red_fill_factor","object_fl_red_asymmetry","object_fl_red_number_of_cells","object_fl_red_first","object_fl_red_last","object_fl_red_minimum","object_fl_red_sws_covariance"]

    data_listmode= [
        [sample_name+"_0",sample_name,20,5.351,3.072,3416,405.8,178.8,0.3903,9.013,0.625,0.05128,1.067,23.82,18.41,18.41,6.305E+05,3.688,278.4,30.73,14.41,0.3398,10.66,0.6481,0.1217,1.021,0.7315,4.582,0.7315,13.87,9.08,24.83,1.604,1.269,0.7864,8.475,0.9654,0.1079,1.081,1.148,0.7214,0.7214,614.7,4.647,51.16,4.738,2.64,0.4669,9.552,0.7526,0.005478,1.026,0.5998,1.008,0.5998,7032,4.821,161.2,15.32,8.35,0.4637,9.737,0.7452,0.02497,1.003,1.222,2.59,1.222,2.524E+04,6.609,-4.172E-07,0.05819,-0.00306,3.614E+06,-58.71,1.226E-13,7.18,1.261,-0.1321,0.05813,-0.1442,1.979],
        [sample_name+"_1",sample_name,20,5.351,3.242,3389,393.9,177.6,0.395,8.529,0.6239,0.1022,1.06,31.98,15.13,15.13,1.087E+06,3.649,431.3,47.81,22.43,0.384,10,0.6568,0.05274,1.037,1.997,5.184,1.997,21.69,6.862,22.85,1.647,1.173,0.6488,8.756,0.8981,0.07829,1.004,0.7354,0.5653,0.5653,1892,5.133,43.46,3.712,2.232,0.6023,9.257,0.8576,0.02558,1.1,1.191,1.059,1.059,6593,4.779,148.3,13.62,7.67,0.5031,9.184,0.7709,0.0333,1.019,1.926,2.554,1.926,3.411E+04,0.2,-1.788E-06,0.1257,-0.006614,7.736E+05,-17.25,3.447E-12,2.816,1.379,-0.06356,0.1257,-0.08305,0.6221],
        [sample_name+"_2",sample_name,24,5.351,3.866,4262,453.6,184.7,0.3316,11.19,0.5719,0.02655,1.091,10.78,14.12,10.78,1.28E+06,4.17,444.7,44.89,19.16,0.3221,12.69,0.593,0.103,1.073,0.9985,3.966,0.9985,20.7,5.34,28.62,2.16,1.215,0.6038,11.82,0.8506,0.02826,1.209,0.5711,0.6684,0.5711,2940,4.849,68.48,6.102,2.948,0.4393,11.82,0.6888,0.02783,1.082,0.5191,0.6757,0.5191,1.386E+04,5.647,229.2,18.86,9.865,0.45,11.61,0.7138,0.009214,1.013,1.02,2.274,1.02,4.571E+04,0.2,-8.345E-07,0.1163,-0.005059,2E+06,-21.65,5.515E-13,2.882,1.916,0.03938,0.1163,-0.08402,1.075],
        [sample_name+"_3",sample_name,20,5.351,3.256,2894,339.5,151.4,0.3707,9.354,0.6163,0.01538,1.057,11.27,17.46,11.27,6.416E+05,3.514,308.1,34.86,15.93,0.3145,10.87,0.6319,0.1445,1.025,0.7547,5.374,0.7547,15.54,5.682,16,1.169,0.7923,0.6287,10.54,0.9074,0.1094,0.8763,0.5721,0.947,0.5,1014,4.763,39.43,3.485,2.013,0.5211,9.82,0.827,0.0337,1.046,0.7021,1.191,0.7021,4994,4.537,128.2,12.34,6.603,0.4355,10.05,0.7417,0.0577,1.005,0.9766,2.745,0.9766,2.441E+04,9.456,-5.96E-07,0.1379,-0.007259,1.735E+06,-5.102,3.206E-13,1.537,2.117,0.09018,0.1379,-0.07126,2.533],
        [sample_name+"_29",sample_name,32,5.318,4.763,7603,709,245.1,0.2399,14.8,0.4822,0.04495,1.167,2.086,5.08,2.086,2.34E+06,4.976,532.3,47.81,17.13,0.2629,16.3,0.5072,0.05141,1.158,0.7351,1.422,0.6862,21.88,5.228,45.49,3.332,1.451,0.4611,16.29,0.6765,0.05125,1.21,0.5,0.5125,0.5,7818,5.597,205.3,16.18,6.592,0.345,15.59,0.5835,0.005944,1.122,0.7439,0.942,0.718,5.014E+04,5.962,766.9,59.38,24.66,0.3166,15.55,0.5724,0.003501,1.076,0.5,2.554,0.5,1.888E+05,0.2,3.874E-06,0.5652,-0.008723,7087,35.22,6.246E-13,1.272,2.22,0.5652,0.2704,-0.1377,9.992],
        [sample_name+"_3269",sample_name,40,177.5,5.041,7898,709,202.5,0.1654,18.72,0.3985,0.03977,1.307,1.574,2.111,1.574,5.68E+07,5.977,5604,432.9,143.6,0.2078,19.7,0.4532,0.01041,1.196,1.749,2.04,1.693,202.1,5.803,204.5,15.32,5.23,0.2672,18.96,0.4918,0.02788,1.219,0.6596,0.5,0.5,1.182E+06,5.774,837.1,66.18,21.44,0.213,18.59,0.4507,0.04679,1.225,0.5572,0.8392,0.5378,5.077E+06,5.901,3280,251.8,84.04,0.2247,18.82,0.4654,0.03475,1.196,1.59,2.26,1.479,1.967E+07,19.48,-1.013E-06,0.4846,-0.007299,7.38E+06,154.9,1.776E-14,6.944,1.601,0.4846,0.2846,-0.2136,-1581],
        [sample_name+"_3543",sample_name,64,193.5,10.81,2.977E+04,1358,472.3,0.2278,28.84,0.4848,0.08455,1.151,11.64,11.07,11.07,1.973E+08,14.73,3.394E+04,1059,536.8,0.4457,30.98,0.6851,0.01661,1.13,145.1,118.3,118.3,496.8,11.5,1118,47.36,17.73,0.2575,29.49,0.5132,0.06383,1.141,0.6532,0.8396,0.6445,7.95E+06,11.33,5043,219.9,80.04,0.2248,29.13,0.4866,0.07521,1.126,1.266,1.149,0.9245,3.537E+07,11.36,2.213E+04,958,351.2,0.2282,29.3,0.4898,0.06982,1.131,5.362,4.164,4.164,1.586E+08,12.96,-1.997E-06,0.188,-0.002462,1.357E+07,-952.8,4.812E-14,31.25,1.717,-0.1825,0.1551,-0.2431,107.3],
        [sample_name+"_4206",sample_name,84,230.6,27.75,7.94E10104,72,555.1,19.87,1.807E+04,714.5,254.5,0.4321,33.32,0.552,0.06147,2.984,1.586,3.026,1.586,5.063E+07,20.1,4324,135,60.89,0.4714,36.31,0.6812,0.02287,1.815,1.058,1.333,1.058,49.87,21.15,370.7,12.02,5.214,0.5107,35.35,0.6485,0.004092,2.56,0.5375,0.5,0.5,7.987E+05,20.96,1498,48.23,21.09,0.4837,34.78,0.6267,0.02037,2.487,0.9041,0.9021,0.9002,3.592E+06,20.92,6258,201.1,88.11,0.4703,35.09,0.6222,0.01147,2.383,3.08,2.23,2.23,1.521E+07,35.49,-1.252E-05,0.6892,-0.006328,1.003E+06,0.6974,5.692E-13,0.9804,2.613,0.6892,0.4493,-0.2329,-2148],
        [sample_name+"_10104",sample_name,1502,955.5,0.5331,41.69,0.7534,0.004633,1.459,55.79,89.54,55.79,-9.255E+06,41.49,6775,95.81,80.65,0.9274,42.24,0.9846,0.01772,2.595,80.46,81.42,53.75,4.517,26.97,233,4.956,2.8,0.5899,41.92,0.7816,0.01012,1.787,0.5,0.5921,0.5,-4.315E+04,28.25,864.7,17.7,10.4,0.5909,41.89,0.7727,0.009397,1.706,0.6139,1.196,0.6139,-1.924E+05,28.34,4234,81.42,50.96,0.5748,42.09,0.7685,0.01425,1.557,2.866,4.372,2.866,-8.632E+05,40.05,8.225E-06,0.03831,4.93E-05,9.731E+04,-1261,4.236E-11,31.38,14.8,0.02497,-0.004083,-0.0266,-0.01192],
    ]

    type_header_listmode = ["[t]","[t]"]+["[f]" for _ in range(len(header_listmode)-2)]

    def __init__(self):
        print("header len:" + str(len(self.header)))
        self.df = pd.DataFrame(columns=[key for key in self.header])
        self.df.to_csv("tests/cytosense/result/" + self.sample_name + "__test_1__" + ".csv", index=False)

        # df = df.reindex(sorted(df.columns), axis=1)

        self.df.loc[len(self.df)]=self.type_header
        for values in self.data_pulse:
            d = {}
            for index, key in enumerate(self.header):
                d[key]= values[index]
            print("append row")
            self.df.loc[len(self.df)]=d

        self.df.to_csv("tests/cytosense/result/" + self.sample_name + "__test_2__" + ".csv", index=False)


        # ####################################################################################################


        self.df_listmode = pd.DataFrame(columns=[key for key in self.header_listmode])
        self.df_listmode.to_csv("tests/cytosense/result/" + self.sample_name + "__listmode__test_1__" + ".csv", index=False)

        # df = df.reindex(sorted(df.columns), axis=1)

        self.df_listmode.loc[len(self.df_listmode)]=self.type_header_listmode
        for values in self.data_listmode:
            d = {}
            for index,key in enumerate(self.header_listmode):
                # if index == 1: 
                #     d[key]= self.sample_name
                # else:
                    d[key]= values[index]
            print("append row")
            self.df_listmode.loc[len(self.df_listmode)]=d

        self.df_listmode.to_csv("tests/cytosense/result/" + self.sample_name + "__listmode__test_2__" + ".csv", index=False)



class mock_ulco_dataframe():
    
    local_path = "tests/cytosense/ULCO/mock_small_data"
    mock_path = "tests/cytosense/ULCO/DataFrame"
    # result_path = "tests/cytosense/result/"
    
    sample_name = "R4_photos_flr16_2uls_10min 2022-09-14 12h28"
    
    pulse_filename = sample_name + "__pulses__" + ".csv"
    listmode_filename = sample_name + "__listmode__" + ".csv"
    result_filename = sample_name + "__merge_p_l__" + ".csv"
    
    pulse_path = PurePath(mock_path , pulse_filename)
    listmode_path = PurePath(mock_path , listmode_filename)
    result_path = PurePath(mock_path, result_filename)

    data = {
        'raw_folder': PurePath(local_path),
        'sample_name': sample_name,
    }

    def __init__(self):
        self.df_pulses = pd.read_csv(self.pulse_path)
        self.df_listmode = pd.read_csv(self.listmode_path)

        self.df = pd.merge(self.df_pulses, self.df_listmode, how="inner", on=["object_id"])
        self.df.to_csv(self.result_path, index=False)

        self.data['tsv_pulse']={}
        self.data['tsv_pulse']['dataframe']=self.df_pulses
        self.data['tsv_listmode']={}
        self.data['tsv_listmode']['dataframe']=self.df_listmode



def test():
        mock = mock_ulco_small_data()
        local_path = mock.local_path
        sample_name = mock.sample_name
        polynomial_filename = mock.polynomial_filename
        corrupted_model = mock.model
        dftest = mock.df

def test2():
        mock = mock_ulco_dataframe()

        print(mock.df_pulses)
        print(mock.df_listmode)
        print(mock.df)


if __name__ == '__main__':
    test2()

