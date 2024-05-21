<template>
    <div>
      <h1>환율 정보</h1>
      <select v-model="nation">
        <option v-for="currency in store.currencies" :key="currency.id">{{ currency.cur_nm }}</option>
      </select>
      <input type="number" v-model="foreign">
      <button @click="convertToKRW">$</button>
      <input type="number" v-model="KRW">
      <button @click="convertToForeign">₩</button>
    </div>
  </template>
  
  <script setup>
    import { useCounterStore } from '@/stores/counter'
    import { onMounted, ref, watch, computed } from 'vue'
  
    const store = useCounterStore()
    onMounted(() => {
      store.getCurrency()
    })
  
    const nation = ref(null)
    const currency = computed(() => {
      return store.currencies.find(currency => currency.cur_nm === nation.value)
    })
  
    const KRW = ref(0)
    const foreign = ref(0)
  
    const convertToForeign = () => {
      if (currency.value) {
        foreign.value = KRW.value / currency.value.bkpr
      }
    }
  
    const convertToKRW = () => {
      if (currency.value) {
        KRW.value = foreign.value * currency.value.bkpr
      }
    }
  </script>
  
  <style scoped>
  
  </style>