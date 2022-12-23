import "../../styles/home/recommendations.css"

const Recommendations = () => {
    return (
        <div className="recommend">
            <h1>
                Recommendations
            </h1>
            <div className="Items">
                <div className="apartmentItem">
                    <img src="/mstile-150x150.png" alt="ApartmentPhoto"/>
                    <div className="itemData">
                        <span>11 000 uah</span>
                        <span>вул. Каспрука Павла, 50</span>
                        <span>Шевченківський, Чернівці</span>
                        <div className="area">
                            <span>2 кімнати</span>
                            <span>.</span>
                            <span>74 м2</span>
                        </div>
                    </div>
                </div>
                <div className="apartmentItem">
                    <img src="/mstile-150x150.png" alt="ApartmentPhoto"/>
                    <div className="itemData">
                        <span>11 000 uah</span>
                        <span>вул. Каспрука Павла, 50</span>
                        <span>Шевченківський, Чернівці</span>
                        <div className="area">
                            <span>2 кімнати</span>
                            <span>.</span>
                            <span>74 м2</span>
                        </div>
                    </div>
                </div>
                <div className="apartmentItem">
                    <img src="/mstile-150x150.png" alt="ApartmentPhoto"/>
                    <div className="itemData">
                        <span>11 000 uah</span>
                        <span>вул. Каспрука Павла, 50</span>
                        <span>Шевченківський, Чернівці</span>
                        <div className="area">
                            <span>2 кімнати</span>
                            <span>.</span>
                            <span>74 м2</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Recommendations