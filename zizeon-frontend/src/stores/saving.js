import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useSavingStore = defineStore('savingcounter', () => {
  const savings = ref([])
  const savingoptions = ref([])
  const API_URL = 'http://70.12.102.186:8000'

  const getSaving = function() {
    axios({
      method: 'get',
      url: `${API_URL}/products/saving/`
    })
    .then(res => {
      savings.value = res.data.savings
      savingoptions.value = res.data.options
    })
    .catch(err => console.log(err))
  }

  return { savings, API_URL, getSaving, savingoptions }
}, { persist : true } )