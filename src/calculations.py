
def calculate_future_value(principal: int, gross_annual_return: float, compounds_per_year: int, years: int):
	if compounds_per_year == 0:
		return 0

	compounding_periods = compounds_per_year * years

	return principal * pow( 1 + ( gross_annual_return / compounds_per_year ), compounding_periods)


# Principal * pow( 1 + (Gross Annual Return/Compounding Per Year), Compounding Periods)
# Principal * pow( 1 + (Net Annual Return/Compounding Per Year), Compounding Periods)

