<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-lg-6 col-12">
        <h2>Skills and Career Goals</h2>

        <ul class="nav nav-tabs" id="myTab" role="tablist">
          <li class="nav-item" role="presentation">
            <button
              class="nav-link active"
              id="home-tab"
              data-bs-toggle="tab"
              data-bs-target="#home"
              type="button"
              role="tab"
              aria-controls="home"
              aria-selected="true"
            >
              Technical Skills
            </button>
          </li>
          <li class="nav-item" role="presentation">
            <button
              class="nav-link"
              id="profile-tab"
              data-bs-toggle="tab"
              data-bs-target="#profile"
              type="button"
              role="tab"
              aria-controls="profile"
              aria-selected="false"
            >
              Soft Skills
            </button>
          </li>
          <li class="nav-item" role="presentation">
            <button
              class="nav-link"
              id="contact-tab"
              data-bs-toggle="tab"
              data-bs-target="#contact"
              type="button"
              role="tab"
              aria-controls="contact"
              aria-selected="false"
            >
              Contact
            </button>
          </li>
        </ul>
        <div class="tab-content" id="myTabContent">
          <div
            class="tab-pane fade show active"
            id="home"
            role="tabpanel"
            aria-labelledby="home-tab"
          >
            <TechnicalSkills @send-data="CTSList" />
          </div>
          <div
            class="tab-pane fade"
            id="profile"
            role="tabpanel"
            aria-labelledby="profile-tab"
          >
            <SoftSkills @send-data="CSKList" />
          </div>
          <div
            class="tab-pane fade"
            id="contact"
            role="tabpanel"
            aria-labelledby="contact-tab"
          >
            ...
          </div>
        </div>
      </div>
      <div class="col">
        <h2>Gaps and Job recommandations</h2>
        <p>Loading....</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import TechnicalSkills from "../components/TechnicalSkill.vue";
import SoftSkills from "../components/SoftSkill.vue";
import { ref } from "vue";

const PTSList = ref([]);

const CTSList = (data) => {
  PTSList.value = data;
};

const PSKList = ref([]);
const CSKList = (data) => {
  PSKList.value = data;
  console.log(PSKList.value);
};
</script>
<style scoped></style>
