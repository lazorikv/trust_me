import "../../styles/home/homepage.css"
import Intro from "./Intro";
import Recommendations from "./Recommendations.js";
import Article from "./Article";

const HomeScreen = () => {

    return (
        <div>
            <Intro/>
            <Recommendations/>
            <Article/>
        </div>

    )

}

export default HomeScreen
