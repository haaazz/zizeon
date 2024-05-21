<template>
  <div>
    <h1>마이페이지</h1>
    <h3>가입한 적금 목록</h3>
    <ul>
      <li v-for="saving in savings" :key="saving.id">
        <p v-for="s in savingsInfo(saving.saving)">{{ s }}</p>
      </li>
    </ul>
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { useSavingStore } from '@/stores/saving'
  import { useUserStore } from '@/stores/user'
  import { ref, onMounted } from 'vue'

  const store = useSavingStore()
  const userstore = useUserStore()

  const savings = ref([])

  const savingsInfo = function (pk) {
    return store.savings.filter((saving) => saving.id === pk)
  }

  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/accounts/savings/`,
      headers: {
        Authorization: `Token ${userstore.token}`
      }
    })
      .then((response) => {
        savings.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  })
</script>

<style scoped>

</style>