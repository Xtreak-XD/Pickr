import numpy as np
from scipy.sparse import coo_matrix, csr_matrix
from sklearn.preprocessing import normalize
from sklearn.metrics.pairwise import cosine_similarity

def create_user_item_matrix(interactions):
    """
    Builds a sparse user-item matrix from interactions data.
    
    Args:
        interactions: DataFrame with columns ['user_id', 'item_id', 'rating']
    
    Returns:
        csr_matrix: Sparse user-item matrix
    """
    user_ids = interactions['user_id'].values
    item_ids = interactions['item_id'].values
    ratings = interactions['rating'].values

    n_users = len(interactions['user_id'].unique())
    n_items = len(interactions['item_id'].unique())
    
    matrix = coo_matrix((ratings, (user_ids, item_ids)), shape=(n_users, n_items))
    return matrix.tocsr()

def compute_item_similarity(user_item_matrix):
    """
    Computes item-item cosine similarity matrix.
    
    Args:
        user_item_matrix: Sparse user-item matrix
    
    Returns:
        ndarray: Item-item similarity matrix
    """

    item_user_matrix = user_item_matrix.T
    
    item_similarity = cosine_similarity(item_user_matrix)
    
    return item_similarity

def get_user_seen_items(user_id, user_item_matrix):
    """
    Get items that a user has already interacted with.
    
    Args:
        user_id: Target user ID
        user_item_matrix: Sparse user-item matrix
    
    Returns:
        set: Set of item IDs the user has seen
    """
    user_row = user_item_matrix[user_id]
    seen_items = set(user_row.nonzero()[1])
    return seen_items

def score_items_for_user(user_id, user_item_matrix, item_similarity):
    """
    Scores all items for a target user based on item-item similarity.
    
    Args:
        user_id: Target user ID
        user_item_matrix: Sparse user-item matrix
        item_similarity: Item-item similarity matrix
    
    Returns:
        ndarray: Scores for all items
    """

    user_ratings = user_item_matrix[user_id].toarray().flatten()
    
    item_scores = item_similarity.dot(user_ratings)
    
    return item_scores

def get_recommendations(user_id, user_item_matrix, top_n=5, exclude_seen=True):
    """
    Get Top-N recommendations for a user.
    
    Args:
        user_id: Target user ID
        user_item_matrix: Sparse user-item matrix
        top_n: Number of recommendations to return
        exclude_seen: Whether to exclude items user has already seen
    
    Returns:
        list: Top-N recommended item IDs with scores
    """
    item_similarity = compute_item_similarity(user_item_matrix)
    
    item_scores = score_items_for_user(user_id, user_item_matrix, item_similarity)
    
    if exclude_seen:
        seen_items = get_user_seen_items(user_id, user_item_matrix)
        for item_id in seen_items:
            item_scores[item_id] = -1
    
    top_item_indices = np.argsort(item_scores)[-top_n:][::-1]
    
    recommendations = []
    for item_id in top_item_indices:
        if item_scores[item_id] > 0: 
            recommendations.append({
                'item_id': int(item_id),
                'score': float(item_scores[item_id])
            })
    
    return recommendations

def print_recommendations(user_id, recommendations):
    """
    Prints Top-N recommendations in a formatted way.
    
    Args:
        user_id: Target user ID
        recommendations: List of recommendation dictionaries
    """
    print(f"\n Top-{len(recommendations)} Recommendations for User {user_id}:")
    print("-" * 50)
    
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. Item ID: {rec['item_id']:<8} | Score: {rec['score']:.4f}")
    
    if not recommendations:
        print("No recommendations available.")
    print("-" * 50)

# Example usage function
def run_recommendation_system(interactions_df, target_user_id, top_n=5):
    """
    Complete recommendation pipeline.
    
    Args:
        interactions_df: DataFrame with user interactions
        target_user_id: User to get recommendations for
        top_n: Number of recommendations
    """
    print(f" Building recommendation")
    
    print(" Creating user-item matrix")
    user_item_matrix = create_user_item_matrix(interactions_df)
    print(f"   Matrix shape: {user_item_matrix.shape}")
    
    print(" Computing recommendations...")
    recommendations = get_recommendations(target_user_id, user_item_matrix, top_n)
    
    print_recommendations(target_user_id, recommendations)
    
    return recommendations