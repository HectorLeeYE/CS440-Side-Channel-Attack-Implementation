import dancingCat from "../static/good-morning.gif";

function Landing() {
  return (
    <div>
      <h1>Welcome to the Landing!</h1>
      <p>I hope you visited this page legitimately and didn't just access the endpoint! 😡</p>
      <img src={dancingCat} alt="Dancing Cat" />
    </div>
  );
}

export default Landing;
