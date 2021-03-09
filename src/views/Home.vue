<template>
  <div class="home">
    <el-container>
      <el-header>
        <h1>单词挑战</h1>
      </el-header>
      <el-main>
        <!-- 开始 -->
        <div style="margin: 100px"></div>
        <el-button
          type="primary"
          round
          @click="
            () =>
              this.$router.push({ name: 'Grade', params: { grades: grades } })
          "
          >开始</el-button
        >
      </el-main>
    </el-container>
  </div>
</template>

<script>
import wordsJson from "../assets/word.json";

export default {
  name: "Home",
  data() {
    return {
      grades: wordsJson,
    };
  },
};
</script>
