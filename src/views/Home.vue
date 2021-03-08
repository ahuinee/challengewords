<template>
  <div class="home">
    <el-container>
      <el-header>
        <h1>单词挑战</h1>
      </el-header>
      <el-main>
        <!-- 开始 -->
        <div style="margin: 100px;"></div>
        <router-link to="/grade">
          <el-button type="primary" round >开始</el-button>
        </router-link>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Home",
};
</script>
