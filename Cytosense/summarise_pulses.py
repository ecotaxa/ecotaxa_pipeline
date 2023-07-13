from pathlib import Path
import pandas as pd
import numpy as np
# from tqdm import tqdm


def test_argument(csv_configuration):
    if not ( 'delimiter' in csv_configuration and 'decimal' in csv_configuration):
     raise CSVException("Your csv_configuration argument is not conform to its structure")


#TODO put this functions in the summarize_csv_pulse task class, thus Particle ID could be filtered and we would gain some speed in processing the file as due to the Cytosense process a lot of particle images are not present (not need to sum them)

def summarise_pulses(name, csv_configuration={ 'delimiter' : ',' , 'decimal' : '.' }, show_pulse=False ):
  print("summarizing pulse: " + str(name))

  test_argument(csv_configuration)
  try:
    # 1/ Read one pulse file
    # read
    df = pd.read_csv(name, sep=csv_configuration['delimiter'], decimal=csv_configuration['decimal'])

    #TODO need to verify the structure with the mapping, that permit to control if we are using the good cvs_configuration 

    # # 2/ Fit one pulse shape, to test
    # # get one
    # pulse = df.loc[df['Particle ID'] == 1]['FWS'].values
    # # fit the pulse
    # n_poly = 10 # number of coefficients to extract
    # n = len(pulse)
    # x = np.linspace(1, n, n)
    # poly = np.polynomial.polynomial.Polynomial.fit(x=x, y=pulse, deg=n_poly-1)
    # # get coefficients
    # coefficients = poly.convert().coef
    # # and plot the polynomial fit


    # from matplotlib import pyplot as plt
    # x,pulse_fitted = poly.linspace(n=n, domain=[1,n])
    # plt.figure()
    # plt.plot(x, pulse, '.', x, pulse_fitted)
    # if show_pulse:
    #   plt.show()
    # plt.savefig('foo.png', bbox_inches='tight')
    

    # # 3a/ Fit all polynomials
    # n_poly = 10
    # fits = []
    # pids = df['Particle ID'].unique()
    # channels = list(df.drop('Particle ID', axis='columns').columns.values)
    # for pid in pids:
    #   # get this particle
    #   pulses = df.loc[df['Particle ID'] == pid]
    #   n = pulses.shape[0]
    #   x = np.linspace(1, n, n)
    #   for channel in channels:
    #     # print('pid:', pid, '  channel:', channel)
    #     poly = np.polynomial.polynomial.Polynomial.fit(x=x, y=pulses[channel].values, deg=n_poly-1)
    #     coefs = poly.convert().coef
    #     fits.append(dict(zip(['particle_ID', 'channel']+['coef_' + str(i) for i in range(n_poly)], [pid, channel]+coefs.tolist())))
    # # -> looong because the .loc[] is long

    # # reformat with channels next to each other in a DataFrame
    # fits = pd.DataFrame(fits)
    # fits = fits.pivot(index='particle_ID', columns='channel')
    # fits.columns = ['_'.join(col).strip() for col in fits.columns.values]


    # 3b/ Fit all polynomials with pandas tools
    n_poly = 10

    # convert DataFrame into the long format, where channels are underneath each other instead of next to each other
    df_long = pd.melt(df, id_vars='Particle ID', var_name='channel', value_name='value')

    def fit_poly(df, n_poly):
        n = df.shape[0]
        # make the polynomial fit
        poly = np.polynomial.polynomial.Polynomial.fit(x=np.linspace(1, n, n), y=df['value'].values, deg=n_poly-1)
        coefs = poly.convert().coef
        return(coefs)
      
    # fit the polynomials to each channel of each particle
    fits = df_long.groupby(['Particle ID', 'channel']).apply(fit_poly, n_poly=n_poly)

    # reformat 
    fits = fits.unstack()

    # reformat with channels next to each other
    final = pd.DataFrame({'Particle ID': fits.index.values})
    channels = list(df.drop('Particle ID', axis='columns').columns.values)
    for channel in channels:
      final = pd.concat(
        [final,
        pd.DataFrame(fits[channel].to_list(), columns=[channel + '_coef_' + str(i) for i in range(n_poly)])],
        axis=1)
      
  except FileNotFoundError:
    raise CSVException("file: " + name + " don't exist")
  except KeyError:
    raise CSVException("Verify your pulses csv file: your csv_configuration seems to use the wrong delimiter")
  except np.linalg.LinAlgError:
    raise CSVException("Wrong file: " + str(name) + " not a pulses file")
  
  return final

def save_dataframe_to_csv(df, name, csv_configuration={ 'delimiter' : ',' , 'decimal' : '.' }):

  test_argument(csv_configuration)

  filepath = Path(name)  
  filepath.parent.mkdir(parents=True, exist_ok=True)  
  df.to_csv(filepath, index=False, sep=csv_configuration['delimiter'], decimal=csv_configuration['decimal'] )


class CSVException(Exception):
  def __init__(self, *args: object) -> None:
    super().__init__(*args)

