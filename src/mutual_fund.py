
class MutualFund:
	def __init__(
		self,
		name: str,
		annual_contribution: float,
		annual_interest_rate: float,
		expense_ratio: float,
		principal: float,
		):
		self.name = name
		self.annual_contribution = annual_contribution
		self.expense_ratio = expense_ratio
		self.annual_interest_rate = annual_interest_rate
		self.principal = principal

	def net_annual_return(self):
		return self._annual_interest_rate - self._expense_ratio

	def compounding_per_year(self):
		return 4
