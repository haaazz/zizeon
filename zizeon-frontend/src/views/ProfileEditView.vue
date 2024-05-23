<template>
  <div v-if="editedProfile">
    <h1>프로필 수정</h1>
    <form @submit.prevent="updateProfile">
      <label for="nickname">닉네임:</label>
      <input id="nickname" v-model="editedProfile.nickname" type="text" />

      <label for="job">직업</label>
      <select id="job" v-model="editedProfile.job">
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

      <label for="gender">성별</label>
      <div>
        <label for="Male">남성</label>
        <input
          type="radio"
          id="Male"
          value="Male"
          v-model="editedProfile.gender"
        />

        <label for="Female">여성</label>
        <input
          type="radio"
          id="Female"
          value="Female"
          v-model="editedProfile.gender"
        />
      </div>

      <button type="submit">완료</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useUserStore } from "@/stores/user";
import router from "@/router";

const editedProfile = ref({});
const store = useUserStore();

const updateProfile = () => {
  console.log(editedProfile.value.name);
  axios({
    method: "put",
    url: `${store.API_URL}/accounts/update/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
    data: editedProfile.value,
  })
    .then((response) => {
      console.log("성공!");
      router.push("/mypage");
    })
    .catch((error) => {
      console.log("실패!");
      console.error(error);
    });
};
</script>
