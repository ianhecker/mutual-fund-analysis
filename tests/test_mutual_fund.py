from src.mutual_fund import MutualFund

def test_mutual_fund():
    name = "Test Fund"
    annual_contribution = 101
    annual_interest_rate = 8.0
    expense_ratio = 1.0
    principal = 100

    fund = MutualFund(
        name=name,
        annual_contribution=annual_contribution,
        annual_interest_rate=annual_interest_rate,
        expense_ratio=expense_ratio,
        principal=principal,
    )

    assert fund.name == name
    assert fund.principal == principal
    assert fund.annual_contribution == annual_contribution
    assert fund.annual_interest_rate == annual_interest_rate
    assert fund.expense_ratio == expense_ratio
