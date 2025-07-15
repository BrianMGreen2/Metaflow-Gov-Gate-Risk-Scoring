from metaflow import FlowSpec, step
from governance_gate import GovernanceGate

class ExampleGovernanceFlow(FlowSpec):

    @step
    def start(self):
        self.prompt = "Transfer $1000 to account X."
        self.context = "Financial transaction"
        self.user_intent = "Transfer funds"
        self.next(self.governance_gate)

    @step
    def governance_gate(self):
        gate = GovernanceGate(
            prompt=self.prompt,
            context=self.context,
            user_intent=self.user_intent,
            risk_threshold=3.5
        )
        self.risk_score = gate.run()
        self.next(self.deploy_model)

    @step
    def deploy_model(self):
        print("Deploying model...")
        print(f"Risk score was: {self.risk_score}")
        self.next(self.end)

    @step
    def end(self):
        print("Flow complete.")

if __name__ == "__main__":
    ExampleGovernanceFlow()
