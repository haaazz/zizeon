<template>
  <div>
    <div class="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8 mt-20">
      <div class="mx-auto w-3/5">
        <h2 class="text-center text-2xl font-bold text-green-600 sm:text-3xl">
          금융 퀴즈를 풀어봐요 👀
        </h2>

        <p class="mx-auto mt-4 max-w-md text-center text-gray-500">
          다양한 금융 퀴즈들이 있으며 <br />
          퀴즈는 랜덤으로 출제됩니다.
        </p>

        <div v-if="randomQuiz">
          <QuizDetail :quiz="randomQuiz" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import QuizDetail from "@/components/QuizDetail.vue";
import { ref } from "vue";

const quizList = ref([
  {
    pk: 1,
    question:
      "통화량이 팽창하고 물가가 올라 화폐가치가 하락하는 현상을 뭐라고 할까요?",
    answer: "인플레이션",
  },
  {
    pk: 2,
    question: "주식을 팔 때의 행위를 무엇이라고 할까요?",
    answer: "매도",
  },
  {
    pk: 3,
    question: "투자에서 리스크와 수익은 어떤 관계에 있나요?",
    answer: "양의 관계",
  },
  {
    pk: 4,
    question: "투자에서 자본을 분산하는 것을 뭐라고 할까요?",
    answer: "다변화",
  },
  { pk: 5, question: "주식을 사는 행위를 무엇이라고 할까요??", answer: "매수" },
  {
    pk: 6,
    question: "회사의 주식을 소유한 사람을 무엇이라고 할까요?",
    answer: "주주",
  },
  {
    pk: 7,
    question:
      "금융 시장에서 주식이나 채권 등을 거래하는 장소를 무엇이라고 할까요?",
    answer: "증권 거래소",
  },
  {
    pk: 8,
    question:
      "정부, 기업 등이 투자자로부터 자금을 빌리기 위해 발행하는 증서는 무엇인가요?",
    answer: "채권",
  },
  {
    pk: 9,
    question: "일정 기간 동안 투자로부터 얻는 수익을 무엇이라고 할까요?",
    answer: "수익률",
  },
  {
    pk: 10,
    question: "주식이나 채권을 처음으로 발행하는 시장을 무엇이라고 할까요?",
    answer: "발행 시장",
  },
  {
    pk: 11,
    question: "주식 시장에서 가격이 급격히 상승하는 현상을 무엇이라고 할까요?",
    answer: "상승세",
  },
  {
    pk: 12,
    question:
      "금융 제품을 판매하거나 구매할 때 지불하는 것을무엇이라고 할까요?",
    answer: "수수료",
  },
  {
    pk: 13,
    question: "주식 시장에서 가격이 급격히 하락하는 현상을 무엇이라고 할까요?",
    answer: "하락세",
  },
]);

const randomQuiz = ref(null);

const pickRandomQuiz = () => {
  const randomIndex = Math.floor(Math.random() * quizList.value.length);
  randomQuiz.value = quizList.value[randomIndex];
};

pickRandomQuiz();
</script>

<style scoped></style>
