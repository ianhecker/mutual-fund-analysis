from src.mutual_fund import MutualFund

def test_mutual_fund():
    name = "Test Fund"
    principal = 100
    annual_contribution = 101
    gross_annual_return = 8.0
    expense_ratio = 1.0

    fund = MutualFund(
        name=name,
        principal=principal,
        annual_contribution=annual_contribution,
        gross_annual_return=gross_annual_return,
        expense_ratio=expense_ratio
    )

    assert fund.name == name
    assert fund.principal == principal
    assert fund.annual_contribution == annual_contribution
    assert fund.gross_annual_return == gross_annual_return
    assert fund.expense_ratio == expense_ratio
