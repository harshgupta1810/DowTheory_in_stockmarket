def analyze_stock_trends(stock_data, index_data):

    moving_average_period=50
    volume_threshold=1.5
    """
    Analyzes stock trends using the Dow Theory principles.

    Args:
        stock_data (DataFrame): Historical stock price data for the specific stock.
        index_data (DataFrame): Historical price data for the market index.
        moving_average_period (int): The period for calculating the moving average (default: 50).
        volume_threshold (float): The threshold for validating volume changes (default: 1.5).

    Returns:
        str: An indication of the prevailing trend based on the Dow Theory principles.
    """

    # Calculate the moving averages for stock and index
    stock_data['SMA'] = stock_data['Close'].rolling(window=moving_average_period).mean()
    index_data['SMA'] = index_data['Close'].rolling(window=moving_average_period).mean()

    # Determine the current trend
    if stock_data['Close'].iloc[-1] > stock_data['SMA'].iloc[-1] and index_data['Close'].iloc[-1] > index_data['SMA'].iloc[-1]:
        trend = "Bullish (Upward Trend)"
    elif stock_data['Close'].iloc[-1] < stock_data['SMA'].iloc[-1] and index_data['Close'].iloc[-1] < index_data['SMA'].iloc[-1]:
        trend = "Bearish (Downward Trend)"
    else:
        trend = "Indecisive (No Clear Trend)"

    # Calculate the volume change
    stock_data['VolumeChange'] = stock_data['Volume'].pct_change()

    # Check for volume confirmation
    if stock_data['VolumeChange'].iloc[-1] > volume_threshold:
        volume_confirmation = "Volume Confirms Trend"
    else:
        volume_confirmation = "Volume Does Not Confirm Trend"

    return f"Current Trend: {trend}\nVolume Confirmation: {volume_confirmation}"