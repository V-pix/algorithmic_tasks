class Competition:
    def _change_score(self, participant_id, change):
        self._scores[participant_id] += change

    def __init__(self, participant_count):
        self._scores = [0] * participant_count

    def like(self, participant_id):
        self._change_score(participant_id, 1)

    def dislike(self, participant_id):
        self._change_score(participant_id, -1)

    def get_best_works(self, count):
        scores_ids = [(value, id) for id, value in enumerate(self._scores)]
        scores_ids.sort(reverse=True)
        return [id for _, id in scores_ids[:count]]

if __name__ == "__main__":
    a = Competition(10)

    # Вызов метода like() для участника с определенным идентификатором
    participant_id = 3
    a.like(participant_id)

    # Вызов метода dislike() для другого участника
    another_participant_id = 7
    a.dislike(another_participant_id)

    # Вызов метода get_best_works() для получения лучших работ
    count = 5
    best_works = a.get_best_works(count)

    # Вывод результатов
    print("Лучшие работы:")
    for work_id in best_works:
        print(f"Работа {work_id}")