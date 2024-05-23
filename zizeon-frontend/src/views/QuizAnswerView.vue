<template>
  <div class="w-3/5 mx-auto pt-10 pb-5 sm:px-6 lg:px-2 rounded-lg shadow-lg mt-8 overflow-auto">
    <div class="title-section">
      <h2 class="answer-title">정답 확인</h2>
    </div>
    <div class="content-section">
      <img
        :src="isCorrect ? correctImage : incorrectImage"
        :alt="isCorrect ? '정답 이미지' : '오답 이미지'"
        class="answer-image"
      />
      <p
        class="result-message"
        :class="{ correct: isCorrect, incorrect: !isCorrect }"
      >
        {{ isCorrect ? "정답입니다!" : "오답입니다." }}
      </p>
      <p
        class="user-answer"
        :class="{ correct: isCorrect, incorrect: !isCorrect }"
      >
        나의 제출 답안: {{ userAnswer }}
        <br />
        <p>정답: {{ answer }}</p>
      </p>
    </div>
    <div class="text-center mt-5">
    <button class="back-button" @click="goBack">뒤로가기</button>
  </div>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from "vue-router";
import correctImage from "@/assets/nopyunsik.png";
import incorrectImage from "@/assets/pyunsik.png";
import { computed } from 'vue'

const route = useRoute();
const router = useRouter();

const { pk, answer } = route.params
const userAnswer = route.query.userAnswer

const isCorrect = computed(() => answer === userAnswer)

const goBack = () => {
  router.push("/quiz");
};
</script>

<style scoped>

.title-section {
  text-align: center;
  margin-bottom: 20px;
}

.answer-title {
  font-size: 24px;
  margin: 0;
}

.quiz-question {
  font-size: 18px;
  margin: 0;
}

.user-answer,
.correct-answer {
  font-size: 16px;
  margin-top: 15px;
}

.answer-image {
  margin: auto;
}

.content-section {
  background: white;
  padding: 20px;
  border-radius: 10px;
  border: 1px solid rgb(199, 199, 199);
  text-align: center;
  justify-content: center;
}
.result-message {
  font-size: 18px;
  font-weight: bold;
  margin-top: 20px;
}

.correct {
  color: #007f00; /* Green for correct answers */
}

.incorrect {
  color: #ff0000; /* Red for incorrect answers */
}
</style>
