<template>
  <div class="main">
    <sui-grid centered :columns="3">
      <sui-grid-column>
        <sui-card-group :items-per-row="3" stackable>
          <sui-card>
            <sui-image
              src="https://semantic-ui.com/images/avatar2/large/kristy.png"
            />
          </sui-card>
          <sui-card>
            <sui-image
              src="https://semantic-ui.com/images/avatar2/large/kristy.png"
            />
          </sui-card>
          <sui-card>
            <sui-image
              src="https://semantic-ui.com/images/avatar2/large/kristy.png"
            />
          </sui-card>
          <sui-card>
            <sui-image
              src="https://semantic-ui.com/images/avatar2/large/kristy.png"
            />
          </sui-card>
          <sui-card>
            <sui-image
              src="https://semantic-ui.com/images/avatar2/large/kristy.png"
            />
          </sui-card>
          <sui-card>
            <sui-image
              src="https://semantic-ui.com/images/avatar2/large/kristy.png"
            />
          </sui-card>
        </sui-card-group>
 
        <sui-rail position="left">
          <sui-segment>
            <sui-image
              src="https://semantic-ui.com/images/avatar/large/nan.jpg"
              size="small"
              circular
              centered
            />
            <sui-container text-align="center" class="details">
              <b>Casandra Luis</b>
              <h5>@casnadra23</h5>
              <p>
                Lorem ipsum dolor, sit amet consectetur adipisicing elit.
                Sapiente, suscipit?
              </p>
            </sui-container>
          </sui-segment>
        </sui-rail>
      </sui-grid-column>
    </sui-grid>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.main {
  margin-top: 7em;
}
.details {
  margin-top: 1em;
}
</style>
