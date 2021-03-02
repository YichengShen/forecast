# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/01_data_transformation.ipynb (unless otherwise specified).

__all__ = ['plot_data']

# Cell
def plot_data(df_dates, prices_dict):
    """
    the second argument requires a dictionary
    """
    # Convert strings to datetime
    dates = [pd.to_datetime(date, format='%Y-%m-%d') for date in df_dates]

    fig, ax = plt.subplots()
    for key, value in prices_dict.items():
        ax.plot(dates, value, label=key)

    # format the ticks
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    # format the coords message box
    ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')

    # rotates and right aligns the x labels, and moves the bottom of the
    # axes up to make room for them
    fig.autofmt_xdate()

    # Only show xtick for every 5 years
    every_nth = 5
    for n, xtick in enumerate(ax.xaxis.get_major_ticks()):
        if n % every_nth != 0:
            xtick.label1.set_visible(False)
            xtick.set_visible(False)

    return fig, ax