
def calculate_future_value_with_expense_ratio(
	principal: int,
	annual_interest_rate: float,
	expense_ratio: float,
	compounds_per_year: int,
	years: int):

	net_annual_interest = annual_interest_rate - expense_ratio

	return calculate_future_value(
		principal,
		net_annual_interest,
		compounds_per_year,
		years)

def calculate_future_value(
	principal: int,
	annual_interest_rate: float,
	compounds_per_year: int,
	years: int):

	if compounds_per_year == 0:
		return 0

	compounding_periods = compounds_per_year * years

	return principal * pow( 1 + ( annual_interest_rate / compounds_per_year ), compounding_periods)


# Principal * pow( 1 + (Gross Annual Return/Compounding Per Year), Compounding Periods)
# Principal * pow( 1 + (Net Annual Return/Compounding Per Year), Compounding Periods)
