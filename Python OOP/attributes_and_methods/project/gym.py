class Gym:
    customers = []
    trainers = []
    equipment = []
    plans = []
    subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        result = ''
        subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        result += (str(subscription) + '\n')
        customer = [c for c in self.customers if c.id == subscription.customer_id][0]
        result += (str(customer) + '\n')
        trainer = [t for t in self.trainers if t.id == subscription.trainer_id][0]
        result += (str(trainer) + '\n')
        plan = [p for p in self.plans if p.id == subscription.exercise_id][0]
        result += (str(plan) + '\n')
        trainer = [t for t in self.trainers if t.id == subscription.trainer_id][0]
        result += (str(trainer) + '\n')
        equipment = [e for e in self.equipment if e.id == plan.equipment_id][0]
        result += str(equipment)
        return result




