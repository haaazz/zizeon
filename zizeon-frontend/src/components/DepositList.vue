<template>
    <div class="content">
      <h1>예금</h1>
      <ul>
        <li v-for="deposit in store.deposits" :key="deposit.id">{{ deposit.fin_prdt_nm }}</li>
      </ul>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useDepositStore } from '@/stores/deposit'
  
  const store = useDepositStore()
  const deposits = ref([])
  
  onMounted(async () => {
    await store.getDeposit()
    deposits.value = store.deposits
  })
  </script>
  
  <style scoped>
  .content {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  </style>
  