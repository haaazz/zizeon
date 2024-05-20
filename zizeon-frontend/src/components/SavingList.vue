<template>
    <div class="content">
      <h1>적금</h1>
      <ul>
        <li v-for="saving in store.savings" :key="saving.id">{{ saving.fin_prdt_nm }}</li>
      </ul>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useSavingStore } from '@/stores/saving'
  
  const store = useSavingStore()
  const savings = ref([])
  
  onMounted(async () => {
    await store.getSaving()
    savings.value = store.savings
  })
  </script>
  
  <style scoped>
  .content {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  </style>
  