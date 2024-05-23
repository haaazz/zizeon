<template>
  <div
    class="mx-auto max-w-screen-xl sm:px-6 lg:px-2 rounded-lg shadow-lg mt-8 overflow-auto"></div>
    <h5 class="text-center text-lg font-medium break-words">{{ quiz.question }}</h5>
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
</template>

<script setup>
import { useRouter } from "vue-router";
import { ref } from "vue";

defineProps({
  quiz: Object,
});

const router = useRouter();
const userAnswer = ref("");

const submitAnswer = function(quiz) {
  router.push({
    name: "answer",
    params: { pk: quiz.pk, answer: quiz.answer },
    query: { userAnswer: userAnswer.value },
  });
};
</script>

<style scoped></style>
