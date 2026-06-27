import re

def solution(message, spoiler_ranges):
    # 각 문자가 몇 번째 스포 방지 구간에 포함되는지 기록
    covered = [-1] * len(message)

    for range_index, (start, end) in enumerate(spoiler_ranges):
        for i in range(start, end + 1):
            covered[i] = range_index

    # 각 스포 구간을 열었을 때 완전히 공개되는 단어
    revealed_words = [[] for _ in spoiler_ranges]
    normal_words = set()

    for match in re.finditer(r"[a-z0-9]+", message):
        word = match.group()
        start, end = match.span()

        # 단어가 포함된 마지막 스포 구간을 열어야 완전히 공개됨
        last_range = max(covered[start:end])

        if last_range == -1:
            normal_words.add(word)
        else:
            revealed_words[last_range].append(word)

    answer = 0
    previously_revealed = set()

    # 스포 구간을 왼쪽부터 순서대로 공개
    for words in revealed_words:
        for word in words:
            if word not in normal_words and word not in previously_revealed:
                answer += 1

            # 중요한 단어가 아니어도 공개된 스포 단어로 기록
            previously_revealed.add(word)

    return answer