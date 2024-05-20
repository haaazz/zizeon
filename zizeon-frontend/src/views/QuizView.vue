<template>
    <div>
      <h1>퀴즈 페이지</h1>
  
      <div v-if="randomQuiz">
        <QuizDetail :quiz="randomQuiz" />
      </div>
    </div>
  </template>
  
  <script setup>
  import QuizDetail from '@/components/QuizDetail.vue'
  import { ref } from 'vue'
  
  const quizList = ref([
    { pk: 1, question: '통화량이 팽창하고 물가가 올라 화폐가치가 하락하는 현상을 뭐라고 할까요?', answer: '인플레이션' },
    { pk: 2, question: '주식을 팔 때의 행위를 무엇이라고 할까요?', answer: '매도' },
    { pk: 3, question: '투자에서 리스크와 수익은 어떤 관계에 있나요?', answer: '양의 관계' },
    { pk: 4, question: '투자에서 자본을 분산하는 것을 뭐라고 할까요?', answer: '다변화' },
    { pk: 5, question: '주식을 사는 행위를 무엇이라고 할까요??', answer: '매수' }
  ])
  
  const randomQuiz = ref(null)
  
  const pickRandomQuiz = () => {
    const randomIndex = Math.floor(Math.random() * quizList.value.length)
    randomQuiz.value = quizList.value[randomIndex]
  }
  
  // 컴포넌트가 마운트될 때 랜덤 퀴즈를 선택합니다.
  pickRandomQuiz()
  </script>
  

<style scoped>

</style>