import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useSavingStore = defineStore('savingcounter', () => {
  const savings = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  const getSaving = function() {
    axios({
      method: 'get',
      url: `${API_URL}/products/saving/`
    })
    .then(res => {
        savings.value = res.data
    })
    .catch(err => console.log(err))
  }

  return { savings, API_URL, getSaving }
}, { persist : true } )