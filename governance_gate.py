import os
import time

class GovernanceGate:
    def __init__(self, prompt, context, user_intent, risk_threshold=3.5, max_wait=3600, poll_interval=30):
        self.prompt = prompt
        self.context = context
        self.user_intent = user_intent
        self.risk_threshold = risk_threshold
        self.max_wait = max_wait
        self.poll_interval = poll_interval

    def score_risk(self):
        # Example scoring logic (customize as needed)
        score_content = 4 if "transfer" in self.prompt.lower() else 1
        score_context = 3 if self.context == "Financial transaction" else 1
        score_intent = 5 if self.user_intent == "Transfer funds" else 1
        risk_score = (score_content + score_context + score_intent) / 3
        return risk_score

    def wait_for_approval(self):
        waited = 0
        while not os.environ.get("HUMAN_APPROVED"):
            if waited >= self.max_wait:
                raise Exception("Approval timeout exceeded")
            print("Awaiting governance sign-off...")
            time.sleep(self.poll_interval)
            waited += self.poll_interval
        print("Human approval received, proceeding.")

    def run(self):
        risk_score = self.score_risk()
        print(f"Calculated risk score: {risk_score}")
        if risk_score >= self.risk_threshold:
            print("High-risk detected: Awaiting human governance sign-off...")
            self.wait_for_approval()
        else:
            print("Risk score below threshold, proceeding automatically.")
        return risk_score
