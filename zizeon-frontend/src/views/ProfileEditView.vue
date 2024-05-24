<template>
    <h1 class="mt-6 text-xl font-bold sm:text-3xl md:text-4xl text-center text-green-600">
    회원정보 수정 페이지
  </h1>
<div v-if="store.loginUser" class="w-4/5 mx-auto mt-12">

<form @submit.prevent="updateProfile">
    <div class="grid gap-6 mb-6 md:grid-cols-2">
        <div>
            <label for="nickname" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">닉네임</label>
            <input type="text" id="nickname" v-model="store.loginUser.nickname" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required />
        </div>
        <div>
            <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">이메일</label>
            <input type="email" id="email" v-model="editedProfile.email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required />
        </div>  
        <div>
            <label for="age" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">나이</label>
            <input type="tel" id="age" v-model="editedProfile.age" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required />
        </div>

        <div>
            <label for="job" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">직업</label>
            <select id="job" v-model="store.loginUser.job" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required>
            <option value="Analyst">어널리스트</option>
            <option value="Teacher">센세</option>
            <option value="Lawyer">변호사</option>
            <option value="Researcher">조사하는사람</option>
            <option value="Photographer">사진작가</option>
            <option value="Manager">마네쟈</option>
            <option value="Writer">작가</option>
            <option value="Designer">디자이너</option>
            <option value="Doctor">의사</option>
            <option value="Artist">예술가</option>
            <option value="Nurse">간호사</option>
            <option value="Chef">요리사</option>
            <option value="Student">학생</option>
            <option value="Engineer">엔지니어</option>
            <option value="Marketer">마케터</option>
            <option value="Developer">Developer</option>
            <option value="Accountant">회계사</option>
        </select>
          </div>

        <div>
            <label for="income" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">연간                 소득</label>
            <input type="text" id="income" v-model="editedProfile.income" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required />
        </div>

        <div>
            <div class="col-span-6 sm:col-span-3 flex items-center justify-start">
              <label for="gender" class="block p-3 text-m font-medium text-gray-900 dark:text-white">성별</label>

            <div class="flex items-center me-4">
              <label for="Male" class="mr-2">남성</label>
            <input type="radio" id="Male" value="Male" v-model="store.loginUser.gender"
            class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
          </div>
          <div class="flex items-center me-4">
              <label for="Female" class="mr-2">여성</label>
            <input type="radio" id="Female" value="Female" v-model="store.loginUser.gender"
            class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
          </div>
        </div>        </div></div>
        <button type="submit" class="border rounded-lg pl-5 pr-5 pt-1 pb-1 ">완료</button>
</form>


</div>

</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useUserStore } from "@/stores/user";
import router from "@/router";

const store = useUserStore();
const editedProfile = ref({})

const updateProfile = () => {
  axios({
    method: "put",
    url: `${store.API_URL}/accounts/update/`,
    headers: {
      Authorization: `Token ${store.loginUser.token}`,
    },
    data: store.loginUser.value,
  })
    .then((response) => {
      console.log("성공!");
      router.push("/mypage");
    })
    .catch((error) => {
      console.log(store.loginUser.nickname)
      console.log("실패!");
      console.error(error);
    });
};

onMounted(() => {
  console.log(store.loginUser.token)
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/update/`,
    headers: {
      Authorization: `Token ${store.loginUser.token}`,
    }
  })
  .then((response) => {
    editedProfile.value = store.loginUser
    console.log(editedProfile.value)
  })
})
</script>
