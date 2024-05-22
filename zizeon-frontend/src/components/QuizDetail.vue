<template>
  <div
    class="ml-1 mr-1 max-w-screen-xl px-4 py-10 sm:px-6 lg:px-2 rounded-lg p-4 shadow-lg mt-8"
  >
    <h5 class="text-center text-lg font-medium">{{ quiz.question }}</h5>
    <div>
      <label for="answer"></label>
      <input
        type="text"
        class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm mt-8"
        v-model="userAnswer"
        @keyup.enter="submitAnswer(quiz)"
        placeholder="정답을 입력해주세요"
      />
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { ref } from "vue";

defineProps({
  quiz: Object,
});

const router = useRouter();
const userAnswer = ref("");

const submitAnswer = (quiz) => {
  const isCorrect =
    quiz.answer.toLowerCase() === userAnswer.value.trim().toLowerCase();
  console.log(answer.value);

  router.push({
    name: "answer",
    params: { pk: quiz.pk, answer: quiz.answer },
    query: { userAnswer: userAnswer.value, isCorrect },
  });
};
</script>

<style scoped></style>
