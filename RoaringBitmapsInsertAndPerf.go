package main

import (
	"fmt"
	"math/rand"
	"time"

	"github.com/RoaringBitmap/roaring"
)

// Function to manage Roaring Bitmaps
func manageBitmaps(restaurantID uint32, bitmaps map[string]*roaring.Bitmap) {
	dishes := []uint32{1, 3, 5, 7} // IDs for north Indian, Asian, Italian, and pizza
	for _, dish := range dishes {
		if rand.Intn(2) == 0 { // Randomly assign dishes to restaurants
			bitmaps[fmt.Sprintf("dish_%d", dish)].Add(restaurantID)
		}
	}

	if rand.Intn(2) == 0 { // Randomly assign status to restaurants
		bitmaps["status"].Add(restaurantID)
	}

	if rand.Intn(2) == 0 { // Randomly assign dine_out to restaurants
		bitmaps["dine_out"].Add(restaurantID)
	}
}

func main() {
	// Seed the random number generator
	rand.Seed(time.Now().UnixNano())

	// Create and manage Roaring Bitmaps
	bitmaps := make(map[string]*roaring.Bitmap)
	keys := []string{"dish_1", "dish_3", "dish_5", "dish_7", "status", "dine_out"}
	for _, key := range keys {
		bitmaps[key] = roaring.New()
	}

	generatedIDs := make(map[uint32]struct{}) // To ensure unique restaurant IDs

	for i := 0; i < 1000000; i++ {
		var restaurantID uint32
		for {
			restaurantID = uint32(rand.Intn(1000000000) + 1)
			if _, exists := generatedIDs[restaurantID]; !exists {
				generatedIDs[restaurantID] = struct{}{}
				break
			}
		}
		manageBitmaps(restaurantID, bitmaps)
	}

	// Start the timer
	startTime := time.Now()

	// Performing Queries
	resultBitmap := roaring.And(bitmaps["dish_7"], bitmaps["status"])
	resultBitmap.And(bitmaps["dine_out"])

	// Stop the timer
	elapsedTime := time.Since(startTime)

	// Print the elapsed time
	fmt.Printf("Query took %d nanoseconds.\n", elapsedTime.Nanoseconds())

	// Getting the size of the serialized bitmap in bytes
	bmBytes, _ := resultBitmap.MarshalBinary()

	// Getting the size in MBs
	sizeMBs := float64(len(bmBytes)) / (1024 * 1024)

	// Printing the size
	fmt.Printf("Size of Serialized Bitmap: %.2f MB\n", sizeMBs)
}
