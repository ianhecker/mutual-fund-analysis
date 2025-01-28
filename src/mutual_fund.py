
class MutualFund:
	def __init__(self, name, principal, annual_contribution, gross_annual_return, expense_ratio):
		self.name = name
		self.principal = principal
		self.annual_contribution = annual_contribution
		self.gross_annual_return = gross_annual_return
		self.expense_ratio = expense_ratio

	def net_annual_return(self):
		return self._gross_annual_return - self._expense_ratio

	def compounding_per_year(self):
		return 4
