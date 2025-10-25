import pandas as pd
import numpy as np
from liftoff.Algorithm import run_recommendation_system, create_user_item_matrix, get_recommendations

def create_sample_data():
    """Create sample interaction data from the provided CSV format."""
    data = {
        'user_id': ['u_100', 'u_100', 'u_100', 'u_200', 'u_200', 'u_300', 'u_300', 'u_300', 'u_400', 'u_400', 'u_400'],
        'item_id': ['A', 'B', 'D', 'B', 'C', 'C', 'D', 'E', 'A', 'E', 'F'],
        'rating': [5, 4, 3, 5, 4, 5, 4, 3, 2, 5, 4]
    }
    return pd.DataFrame(data)

def preprocess_data(df):
    """Convert string IDs to numerical indices for matrix operations."""
    unique_users = df['user_id'].unique()
    unique_items = df['item_id'].unique()
    
    user_to_idx = {user: idx for idx, user in enumerate(unique_users)}
    item_to_idx = {item: idx for idx, item in enumerate(unique_items)}
    
    # Create reverse mappings
    idx_to_user = {idx: user for user, idx in user_to_idx.items()}
    idx_to_item = {idx: item for item, idx in item_to_idx.items()}
    
    df_processed = df.copy()
    df_processed['user_id'] = df_processed['user_id'].map(user_to_idx)
    df_processed['item_id'] = df_processed['item_id'].map(item_to_idx)
    
    return df_processed, user_to_idx, item_to_idx, idx_to_user, idx_to_item

def test_algorithm():
    """Test the recommendation algorithm with sample data."""
    print("Testing Recommendation Algorithm")
    print("=" * 60)
    
    print("Loading sample data.")
    df = create_sample_data()
    print(f"Sample data shape: {df.shape}")
    print("\nOriginal interactions:")
    print(df.to_string(index=False))
    
    print("\nPreprocessing data...")
    df_processed, user_to_idx, item_to_idx, idx_to_user, idx_to_item = preprocess_data(df)
    
    print("\nUser mappings:")
    for orig, idx in user_to_idx.items():
        print(f"  {orig} -> {idx}")
    
    print("\nItem mappings:")
    for orig, idx in item_to_idx.items():
        print(f"  {orig} -> {idx}")
    
    print("\nGenerating recommendations for each user...")
    print("=" * 60)
    
    for user_str in ['u_100', 'u_200', 'u_300', 'u_400']:
        user_idx = user_to_idx[user_str]
        print(f"\nTesting for user: {user_str} (index: {user_idx})")
        
        try:
            user_item_matrix = create_user_item_matrix(df_processed)
            recommendations = get_recommendations(user_idx, user_item_matrix, top_n=3, exclude_seen=True)
            
            print(f"\nTop 3 Recommendations for User {user_str}:")
            print("-" * 50)
            
            if recommendations:
                for i, rec in enumerate(recommendations, 1):
                    item_str = idx_to_item[rec['item_id']]
                    print(f"{i}. Item: {item_str:<8} | Score: {rec['score']:.4f}")
            else:
                print("No new recommendations available.")
            
            user_interactions = df[df['user_id'] == user_str]
            seen_items = user_interactions['item_id'].tolist()
            print(f"Already seen items: {', '.join(seen_items)}")
            
        except Exception as e:
            print(f"Error for user {user_str}: {e}")    

    print("\nMatrix Information:")
    print("-" * 30)
    user_item_matrix = create_user_item_matrix(df_processed)
    print(f"Matrix shape: {user_item_matrix.shape}")
    print(f"Matrix density: {user_item_matrix.nnz / (user_item_matrix.shape[0] * user_item_matrix.shape[1]):.2%}")
    print(f"Total interactions: {user_item_matrix.nnz}")
    
    print("\nAlgorithm test completed!")

if __name__ == "__main__":
    test_algorithm()