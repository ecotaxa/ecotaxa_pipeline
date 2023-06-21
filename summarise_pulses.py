from pathlib import Path
import pandas as pd
import numpy as np
# from tqdm import tqdm


def summarise_pulses(name, show_pulse=False):
  print("summarizing pulse: "+name)
  # 1/ Read one pulse file
  # read
  df = pd.read_csv(name, sep=';', decimal=",")

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
    
  return final

def saveCSV(df, name):
  filepath = Path(name)  
  filepath.parent.mkdir(parents=True, exist_ok=True)  
  df.to_csv(filepath, index=False)
