<template>
  <div class="answer-view">
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
    <button class="back-button" @click="goBack">뒤로가기</button>
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
.answer-view {
  max-width: 600px;
  margin: 30px auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
  border-radius: 10px;
  border: 1px solid rgb(219, 219, 219);
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
}

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

.content-section {
  background: white;
  padding: 20px;
  border-radius: 10px;
  border: 1px solid rgb(199, 199, 199);
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
