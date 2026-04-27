import random
import math

class WaterRationingAI:
    """
    Multi-Objective Q-Learning ajanı.
    Hedef: Su tasarrufunu maksimize ederken mahsul sağlığını kritik eşiğin üstünde tutmak.
    """
    def __init__(self, states, actions, learning_rate=0.1, discount_factor=0.9):
        self.q_table = {}
        self.lr = learning_rate
        self.gamma = discount_factor
        self.actions = actions

    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def choose_action(self, state, epsilon=0.1):
        if random.random() < epsilon:
            return random.choice(self.actions)
        
        q_values = [self.get_q_value(state, a) for a in self.actions]
        max_q = max(q_values)
        return self.actions[q_values.index(max_q)]

    def update(self, state, action, reward, next_state):
        old_q = self.get_q_value(state, action)
        next_max_q = max([self.get_q_value(next_state, a) for a in self.actions])
        
        new_q = old_q + self.lr * (reward + self.gamma * next_max_q - old_q)
        self.q_table[(state, action)] = new_q

def calculate_lchi_reward(state, action, water_consumed):
    """
    LCHI Reward Fonksiyonu:
    Reward = Sağlık_Puanı - log(Su_Tüketimi + 1) * K
    """
    health_impact = 0
    if state == "HIGH_STRESS":
        health_impact = 20 if action == "FULL_IRRIGATION" else (-30 if action == "NO_IRRIGATION" else 5)
    elif state == "MED_STRESS":
        health_impact = 10 if action == "RATIONED_IRRIGATION" else (0 if action == "FULL_IRRIGATION" else -10)
    else: # LOW_STRESS
        health_impact = 15 if action == "NO_IRRIGATION" else -5

    # Su Tüketim Cezası (Logaritmik asimetri)
    water_penalty = math.log(water_consumed + 1) * 10
    
    return health_impact - water_penalty

def simulate_advanced_management():
    actions = ["FULL_IRRIGATION", "RATIONED_IRRIGATION", "NO_IRRIGATION"]
    water_costs = {"FULL_IRRIGATION": 100, "RATIONED_IRRIGATION": 30, "NO_IRRIGATION": 0}
    ai = WaterRationingAI(states="ADV_STRESS", actions=actions)
    
    print("--- LCHI Water AI Training Phase ---")
    for epoch in range(1000):
        state = random.choice(["LOW_STRESS", "MED_STRESS", "HIGH_STRESS"])
        action = ai.choose_action(state)
        
        reward = calculate_lchi_reward(state, action, water_costs[action])
            
        next_state = random.choice(["LOW_STRESS", "MED_STRESS", "HIGH_STRESS"])
        ai.update(state, action, reward, next_state)

    print(f"Optimal Policy Mapping (State -> Best Action):")
    for s in ["LOW_STRESS", "MED_STRESS", "HIGH_STRESS"]:
        best_action = max(actions, key=lambda a: ai.get_q_value(s, a))
        print(f"  {s} => {best_action}")

if __name__ == "__main__":
    simulate_advanced_management()
