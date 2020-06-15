<template>
  <div class="main">
    <sui-grid centered :columns="3">
      <sui-grid-column>
        <!-- <sui-segment> -->
        <sui-image
          src="https://semantic-ui.com/images/avatar2/large/kristy.png"
          fluid
        />

        <sui-comment-group>
          <h3 is="sui-header" dividing>Comments</h3>

          <sui-comment>
            <sui-comment-avatar
              src="https://semantic-ui-vue.github.io/static/images/avatar/small/matt.jpg"
            />
            <sui-comment-content>
              <a is="sui-comment-author">Matt</a>
              <sui-comment-metadata>
                <div>Today at 5:42PM</div>
              </sui-comment-metadata>
              <sui-comment-text>How artistic!</sui-comment-text>
              <sui-comment-actions>
                <sui-comment-action>Reply</sui-comment-action>
              </sui-comment-actions>
            </sui-comment-content>
          </sui-comment>

          <sui-comment>
            <sui-comment-avatar
              src="https://semantic-ui-vue.github.io/static/images/avatar/small/matt.jpg"
            />
            <sui-comment-content>
              <a is="sui-comment-author">Elliot Fu</a>
              <sui-comment-metadata>
                <div>Yesterday at 12:30AM</div>
              </sui-comment-metadata>
              <sui-comment-text>
                <p>
                  This has been very useful for my research. Thanks as well!
                </p>
              </sui-comment-text>
              <sui-comment-actions>
                <sui-comment-action>Reply</sui-comment-action>
              </sui-comment-actions>
            </sui-comment-content>
          </sui-comment>

          <sui-comment>
            <sui-comment-avatar
              src="https://semantic-ui-vue.github.io/static/images/avatar/small/matt.jpg"
            />
            <sui-comment-content>
              <a is="sui-comment-author">Joe Henderson</a>
              <sui-comment-metadata>
                <div>5 days ago</div>
              </sui-comment-metadata>
              <sui-comment-text>
                Dude, this is awesome. Thanks so much
              </sui-comment-text>
              <sui-comment-actions>
                <sui-comment-action>Reply</sui-comment-action>
              </sui-comment-actions>
            </sui-comment-content>
          </sui-comment>

          <sui-form reply>
            <textarea rows="2" class="pri"></textarea>

            <sui-button
              content="Add Reply"
              label-position="left"
              icon="edit"
              primary
              class="pri"
            />
          </sui-form>
        </sui-comment-group>

        <sui-rail position="right">
          <sui-segment>
            <div>
              <sui-image
                src="https://semantic-ui-vue.github.io/static/images/avatar/small/matt.jpg"
                avatar
              />
              <span>Username</span>
            </div>
            <div text-align="left" class="details">
              <b>Description</b>
              <p>
                Lorem ipsum dolor, sit amet consectetur adipisicing elit.
                Sapiente, suscipit?
              </p>
            </div>
            <div class="tags">
              <a is="sui-label" tag>
                Chill
              </a>
              <a is="sui-label" tag>
                Travel
              </a>
              <a is="sui-label" tag>
                Nature
              </a>
            </div>
            <div class="likes">
              <sui-icon
                slot="trigger"
                name="heart"
                color="red"
                size="large"
              /> 2k
            </div>
          </sui-segment>
        </sui-rail>
        <!-- </sui-segment> -->
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

.pri {
  margin-top: 1em;
}
.details {
  margin: 1.5em 0;
}
.tag {
  margin: 5px;
}
.likes {
    margin-top: 1em;
}
</style>
