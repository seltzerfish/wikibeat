% rebase("layout.tpl", title="Store App - Checkout")

<div class="container">
  <div class="row">
    <div class="twelve column" style="margin-top: 10%">
      <h4 style="text-align: center">Checkout</h4>
    </div>
  </div>
  <form action="/add/order/{{order_id}}" method="POST">
    <fieldset>
      <div class="row" style="margin-top: 5%">
        <div class="six columns">
          <label for="name">Product Name</label>
          <input class="u-full-width" id="name" type="text" placeholder="apple" name="name">
        </div>
        <div class="three columns">
          <label for="quantity">Quantity</label>
          <input class="u-full-width" id="quantity" type="number" placeholder="3" name="quantity">
        </div>
      </div>
      <div class="row"><
        <input class="button-primary" type="submit" value="Add Item">
        <a class="button" href="/order/{{order_id}}" style="margin: 3%; margin-left: 0%">Finalize Order</a
      </div>
      % if defined('added'):
      <div class="row">
        % if added:
          <h3 style="color:darkgreen">Item "{{item["name"]}}" Added</h3>
        % else:
          <h3 style="color:darkred">Item "{{item["name"]}}" Not Found</h3>
      </div>
    </fieldset>
  </form>
</div>