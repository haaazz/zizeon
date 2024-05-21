<template>
  <div>
    <h1>디테일</h1>
    <h3>금융상품명: {{ saving.fin_prdt_nm }}</h3>
    <h3>금융회사명: {{ saving.kor_co_nm }}</h3>
    <button @click="open">가입</button>
    <div v-for="option in options">
      <hr>
      <p>적립유형: {{ option.rsrv_type_nm }}</p>
      <p>저축기간: {{ option.save_trm }}</p>
      <p>저축금리: {{ option.intr_rate }}</p>
      <p>최고우대금리: {{ option.intr_rate2 }}</p>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { useSavingStore } from '@/stores/saving'
  import { useRoute } from 'vue-router'
  import axios from 'axios'

  const store = useSavingStore()
  const route = useRoute()
  
  const saving = ref(null)
  const options = ref(null)

  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/products/saving/${route.params.id}/`
    })
      .then((response) => {
        saving.value = response.data.saving
        options.value = response.data.options
      })
      .catch((error) => {
        console.log(error)
      })
  })
</script>

<style scoped>

</style>